import { useState, useEffect, useRef } from "react";

// Check if a message is from the bot
function isBotMessage(chatMessage) {
    return chatMessage.role === "assistant";
}

// Utility function to format the bot's response
function formatBotMessage(content) {
    // Replace `\n` with HTML line breaks
    let formatted = content.replace(/\n/g, "<br>");
    // Replace `**text**` with bold text
    formatted = formatted.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    return formatted;
}

// Format chat history for Ollama API
function formatMessageHistory(messages) {
    return messages
        .map(msg => `${msg.role === "assistant" ? "Assistant" : "Human"}: ${msg.content}`)
        .join('\n\n');
}

function App() {
    const [message, setMessage] = useState("");
    const [isBotTyping, setIsBotTyping] = useState(false);
    const [chatHistory, setChatHistory] = useState([]);
    const chatContainerRef = useRef(null);

    // Scroll to the bottom whenever chat history is updated
    useEffect(() => {
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
        }
    }, [chatHistory]);

    // Handle form submission when the user sends a message
    const submitForm = async (e) => {
        e.preventDefault();

        // Create the user's message and add it to the chat history
        const userMessage = { role: "user", content: message };
        setChatHistory(prevChatHistory => [...prevChatHistory, userMessage]);
        setMessage(""); // Clear the input field

        // Add a temporary placeholder for the bot's response
        const botMessage = { role: "assistant", content: "" };
        setChatHistory(prevChatHistory => [...prevChatHistory, botMessage]);

        try {
            // Format the entire conversation history for context
            const conversationHistory = [...chatHistory, userMessage];
            const formattedPrompt = formatMessageHistory(conversationHistory);

            // Send the conversation history to the Ollama API with streaming enabled
            const response = await fetch("http://localhost:11434/api/generate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    model: "llama3.2:1b",
                    prompt: formattedPrompt + "\n\nAssistant:", // Add a prompt for the assistant to continue
                    stream: true,
                    context: [], // You can optionally store and reuse the context from previous responses
                }),
            });

            if (!response.ok) {
                throw new Error("Error connecting to Ollama API");
            }

            // Process the stream of data
            const reader = response.body.getReader();
            const decoder = new TextDecoder("utf-8");
            let accumulatedResponse = "";

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                // Decode the stream chunk
                const chunk = decoder.decode(value, { stream: true });

                // Split and parse each JSON object in the chunk
                const lines = chunk.split("\n").filter(line => line.trim() !== "");
                for (const line of lines) {
                    try {
                        const json = JSON.parse(line);
                        if (json.response) {
                            // Append the new word to the accumulated response
                            accumulatedResponse += json.response;

                            // Update the bot's message progressively
                            setChatHistory(prevChatHistory => {
                                const updatedChat = [...prevChatHistory];
                                const lastIndex = updatedChat.length - 1;

                                if (isBotMessage(updatedChat[lastIndex])) {
                                    updatedChat[lastIndex] = {
                                        ...updatedChat[lastIndex],
                                        content: formatBotMessage(accumulatedResponse),
                                    };
                                }

                                return updatedChat;
                            });
                        }

                        // Store the context for future use if needed
                        if (json.context) {
                            // You can store this in state if you want to reuse it
                            console.log("Received context:", json.context);
                        }
                    } catch (err) {
                        console.error("Error parsing JSON chunk:", err);
                    }
                }
            }
        } catch (error) {
            console.error("Error:", error);
            setChatHistory(prevChatHistory => [
                ...prevChatHistory.slice(0, -1),
                {
                    role: "assistant",
                    content: "An error occurred. Please try again later.",
                },
            ]);
        }
    };

    return (
        <div className="bg-gray-100 h-screen flex flex-col">
            <div className="container mx-auto p-4 flex flex-col h-full max-w-2xl">
                <h1 className="text-2xl font-bold mb-4">ChatUI with React + Ollama</h1>

                <div
                    className="flex-grow overflow-y-auto mt-4 bg-white rounded shadow p-4 mb-4"
                    ref={chatContainerRef}
                >
                    {chatHistory.map((chatMessage, i) => (
                        <div
                            key={i}
                            className={`mb-2 ${isBotMessage(chatMessage) ? "" : "text-right"}`}
                        >
                            <p className="text-gray-600 text-sm">
                                {isBotMessage(chatMessage) ? "Bot" : "User"}
                            </p>
                            <p
                                className={`p-2 rounded-lg inline-block ${
                                    isBotMessage(chatMessage) ? "bg-green-100" : "bg-blue-100"
                                }`}
                                dangerouslySetInnerHTML={{
                                    __html: isBotMessage(chatMessage)
                                        ? chatMessage.content
                                        : chatMessage.content,
                                }}
                            ></p>
                        </div>
                    ))}
                </div>

                <form className="flex" onSubmit={submitForm}>
                    <input
                        type="text"
                        placeholder="Type your message..."
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        className="flex-grow p-2 rounded-l border border-gray-300 outline-none"
                        disabled = {isBotTyping}
                    />
                    <button
                        type="submit"
                        className="bg-blue-500 text-white px-4 py-2 rounded-r hover:bg-blue-600"
                    >
                        Send
                    </button>
                </form>
            </div>
        </div>
    );
}

export default App;
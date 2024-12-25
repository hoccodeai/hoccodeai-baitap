import client

def process_text(text, operation):
    """
    Processes the given text based on the specified operation (e.g., translate or summarize).
    """
    if operation == "translate":
        target_language = "English"  # Specify the target language
        prompt = f"Translate the following text to {target_language}:\n\n{text}"
    elif operation == "summarize":
        prompt = f"Summarize the following text:\n\n{text}"
    else:
        return "Invalid operation."

    try:
        result = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            stream=False,
            max_completion_tokens=1000,
        )
        return result.choices[0].message.content.strip()
    except Exception as e:
        return f"Error processing text: {e}"

def process_file(input_file, output_file, operation):
    """
    Reads the content of the input file, processes it, and writes the results to the output file.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    processed_content = process_text(content, operation)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(processed_content)

if __name__ == "__main__":
    input_file = "input_file.txt"
    output_file = "output_file.txt"
    operation = "translate"  # Specify the operation: "translate" or "summarize"
    process_file(input_file, output_file, operation)

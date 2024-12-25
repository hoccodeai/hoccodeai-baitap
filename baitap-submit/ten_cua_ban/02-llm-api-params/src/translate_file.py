import client

def translate_text(text, target_language):
    """
    Translates the given text to the target language using OpenAI API.
    """
    prompt = f"Translate the following text to {target_language}:\n\n{text}"
    try:
        return client.generate_chat_response(prompt, isStream=False)
    except Exception as e:
        return f"Error generating translation: {e}"

def translate_file(input_file, output_file, target_language):
    """
    Reads the content of the input file, translates it, and writes the translated content to the output file.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    translated_content = translate_text(content, target_language)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_content)

if __name__ == "__main__":
    input_file = "input_file.txt"
    output_file = "output_file.txt"
    target_language = "English"  # Specify the target language
    translate_file(input_file, output_file, target_language)

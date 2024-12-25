import client
def get_tone():
    """
    Prompts the user to set the tone for the translation or summary.
    """
    print("Please select the tone for the translation or summary:")
    print("1. Formal")
    print("2. Informal")
    print("3. Professional")
    print("4. Casual")
    choice = input("Enter the number corresponding to your choice: ").strip()
    
    tones = {
        "1": "formal",
        "2": "informal",
        "3": "professional",
        "4": "casual"
    }
    
    return tones.get(choice, "neutral")

def translate_text_with_tone(text, target_language, tone):
    """
    Translates the given text to the target language with the specified tone using OpenAI API.
    """
    prompt = f"Translate the following text to {target_language} with a {tone} tone:\n\n{text}"
    try:
        return client.generate_chat_response(prompt, isStream=False)
    except Exception as e:
        return f"Error generating translation: {e}"

if __name__ == "__main__":
    text = "Hello, my name is John. How are you doing today?"
    target_language = "English"  # Specify the target language
    tone = get_tone()
    translated_text = translate_text_with_tone(text, target_language, tone)
    print("\nTranslated Text:\n", translated_text)

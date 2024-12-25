# Chat bot with terminal interface

from fetch_article import summarize_article
import client
import fetch_article
import export_file_code


def main():
    """
    Main function to run the chatbot loop.
    """
    print("Welcome! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        # Extract URL from the user input
        article_url = fetch_article.extract_url(user_input)
        is_export_code = export_file_code.export_code_reg_in_chat(user_input)
        if article_url:
            summary = summarize_article(article_url)
            print("\nArticle Summary:\n", summary)
       

        # Export file code
        elif is_export_code:
            export_file_code.process_file_code(user_input)
            
        else:   
            # Regular chat response
            client.generate_chat_response(user_input)

if __name__ == "__main__":
    main()

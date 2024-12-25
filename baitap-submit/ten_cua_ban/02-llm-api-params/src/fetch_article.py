from bs4 import BeautifulSoup
import urllib.request
import re


def fetch_article(url):
    try:
        # Send a GET request to the website
        response = urllib.request.urlopen(url)
        
        # Check if the request was successful
        if response.status == 200:
            # Get the website content (HTML)
            website_content = response.read().decode('utf-8')
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(website_content, 'html.parser')
            
            # Extract the article content
            article = soup.find('div', id='main-detail')
            if article:
                print("Article content fetched successfully!")
                return article.get_text(strip=True)  # Return the text content of the article
            else:
                print("Failed to find the article content.")
                return None
        else:
            print(f"Failed to fetch the website. Status code: {response.status}")
            return None

    except urllib.error.URLError as e:
        print(f"An error occurred: {e}")
        return None

def summarize_article(url):
    """
    Fetches the article content from the given URL and summarizes it.
    """
    print("\nFetching article content...")
    article_content = fetch_article(url)
    if article_content:
        print("\nSummarizing article content...")
        summary_prompt = f"Summarize the following article in its original language, maintaining the tone, context, and key points. Ensure the summary is concise but retains all critical information and does not change the meaning of the original text. Do not translate or alter the language of the article:\n\n{article_content}"
        return summary_prompt
    else:
        return "Failed to fetch the article content."
    

def extract_url(text):
    """
    Extracts the first URL found in the given text.
    """
    url_pattern = re.compile(r'https?://\S+')
    match = url_pattern.search(text)
    return match.group(0) if match else None
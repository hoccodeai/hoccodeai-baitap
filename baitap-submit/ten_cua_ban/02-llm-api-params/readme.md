# Project Overview

This project provides various functionalities using OpenAI API, including translating text, summarizing articles, and exporting code from chat responses.

## Requirements

- Python 3.x
- OpenAI API key
- Required packages listed in `requirements.txt`

## Setup

1. Clone the repository.
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
3. Set up your OpenAI API key in a `.env` file:
    ```sh
    together_api_key=your_api_key_here
    ```

## Usage

### Translating Text

Use the `translate_file.py` script to translate the content of a file to a specified language.

### Setting Tone

Use the `set_tone.py` script to translate text with a specified tone.

### Processing Files

Use the `process_file.py` script to process the content of a file based on a specified operation (translate or summarize).

### Chatbot Interface

Use the `main.py` script to run a chatbot interface that can summarize articles or export code from chat responses.

### Fetching and Summarizing Articles

Use the `fetch_article.py` script to fetch and summarize articles from a given URL.

### Exporting Code

Use the `export_file_code.py` script to export code from chat responses to a file.

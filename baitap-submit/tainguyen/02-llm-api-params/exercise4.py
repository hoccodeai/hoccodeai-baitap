import sys
import utils
import os

def translate(text, source_lang, target_lang):
    want = "Translate the following content from "+source_lang+" into " + target_lang + ". The translated content should be keep the same meaning and style as the original content."
    question = " ".join([want,":",text])
    messages = [
        {"role":"system", "content": "You are a translator with 10 years experiences in tech domain"},
        {"role":"user","content":question}
    ]

    chat = utils.client.chat.completions.create(
        messages=messages,
        model="gemma2-9b-it",
    )

    return chat.choices[0].message.content


def exercise4():
    chunk_size = 1024
    default_output_file = os.getenv('OUTPUT_FILE_TRANSLATED')
    default_source_lang = "English"
    default_target_lang = "Vietnamese"

    file_path = utils.require_user_input("Enter the path to the file: ")

    if file_path == "e" or file_path == "q":
        return

    source_lang = input("Enter the source language (default is "+default_source_lang+"): ")
    target_lang = input("Enter the target language (default is "+default_target_lang+"): ")
    output_file = input("Enter the output file path (default is "+default_output_file+"): ")

    if source_lang == "":
        source_lang = default_source_lang

    if target_lang == "":
        target_lang = default_target_lang

    if output_file == "":
        output_file = default_output_file

    if file_path == "0":
        return
    

    with open(file_path, "r") as infile, open(output_file,"w") as outfile: 
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                print("=>Let check '"+output_file+"' for the translated content")
                break

            sys.stdout.write("=")
            sys.stdout.flush()
            outfile.write(translate(chunk, source_lang, target_lang))

exercise4()
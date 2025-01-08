import os
from os.path import dirname, join
from time import time

from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# Constants
CHUNK_SIZE = 2000  # Characters per chunk
SUPPORTED_EXTENSIONS = [".txt", ".md", ".pdf"]
TARGET_LANGUAGE = "Japanese"

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, verbose=True)

client = OpenAI(
    base_url=os.environ.get("URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def validate_file(file_path: str) -> tuple[bool, str]:
    """Validate the file path and extension."""
    if not os.path.exists(file_path):
        return False, f"ファイルが見つかりません: {file_path}"

    if not file_path.endswith(tuple(SUPPORTED_EXTENSIONS)):
        return (
            False,
            f"サポートされていない拡張子です。対応形式: {', '.join(SUPPORTED_EXTENSIONS)}",
        )

    return True, "OK"


def read_file(file_path: str) -> tuple[bool, str]:
    """Read content from file based on extension."""
    try:
        _, ext = os.path.splitext(file_path)

        if ext.lower() == ".pdf":
            # PDF file handling
            with open(file_path, "rb") as file:
                pdf_reader = PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                return True, text
        else:
            # Text file handling
            with open(file_path, "r", encoding="utf-8") as file:
                return True, file.read()

    except Exception as e:
        return False, f"ファイル読み込みエラー: {str(e)}"


def write_file(file_path: str, content: str) -> bool:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)

        _, ext = os.path.splitext(file_path)

        if ext.lower() == ".pdf":
            # PDF file handling
            # pdf_writer = PdfWriter()
            print("Coming soon...")
        else:
            # Text file handling
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

        print(f"ファイルが正常に書き込まれました: {file_path}")
        return True
    except Exception as e:
        print(f"ファイル書き込みエラー: {str(e)}")
        return False


def chunk_text(text) -> list[str]:
    """Split text into manageable chunks"""
    return [text[i : i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]


def translate_chunk(chunk: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gemma2-9b-it",
            n=1,
            max_tokens=500,
            temperature=0.7,
            top_p=1,
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are a professional female interpreter, skilled in nuanced and accurate translation.
Your task is to translate the following text into {TARGET_LANGUAGE}.
Please focus on conveying not just the literal meaning, but also the tone, style, and cultural context of the original text.
Consider the target audience as native {TARGET_LANGUAGE} speakers.
                    """,
                },
                {"role": "user", "content": chunk},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"要約中にエラーが発生しました: {str(e)}")
        return None


def main():
    print("PDFファイルパスを入力してください。終了するにはCtrl+Cを押してください。")
    try:
        while True:
            # Input file
            input_pdf_path = input("Path: ")
            if not input_pdf_path.strip():
                continue

            # Validate file
            is_valid, message = validate_file(input_pdf_path)
            if not is_valid:
                print(message)
                continue

            # Create output file path
            base_filename = os.path.basename(input_pdf_path)
            file_name, ext = os.path.splitext(base_filename)
            # output_path = join(dirname(__file__), f"{file_name}_translated{ext}")
            output_path = join(dirname(__file__), f"{file_name}_translated.txt")

            # Read file
            success, content = read_file(input_pdf_path)
            if not success:
                print(content)
                continue

            # Translate
            chunks = chunk_text(content)
            translated_chunks = []

            print(f"全{len(chunks)}チャンクを翻訳中...")
            for i, chunk in enumerate(chunks, 1):
                print(f"チャンク {i}/{len(chunks)} を処理中...")
                translated = translate_chunk(chunk)
                if translated:
                    translated_chunks.append(translated)
                time.sleep(1)  # Avoid rate limit

            # Write file
            if translate_chunk:
                write_file(output_path, "\n".join(translated_chunks))

    except KeyboardInterrupt:
        print("\nプログラムを終了します。お疲れ様でした!")


if __name__ == "__main__":
    main()

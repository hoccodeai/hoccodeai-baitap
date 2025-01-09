import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def read_file(file_path):
    """Đọc nội dung từ file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Lỗi khi đọc file: {str(e)}"

def write_file(content, output_file):
    """Ghi nội dung vào file"""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Lỗi khi ghi file: {str(e)}")
        return False

def split_text(text, max_chunk_size=4000):
    """Chia văn bản thành các phần nhỏ hơn"""
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        word_size = len(word) + 1  # +1 cho khoảng trắng
        if current_size + word_size > max_chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_size = word_size
        else:
            current_chunk.append(word)
            current_size += word_size
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def translate_content(content, source_lang, target_lang):
    """Dịch nội dung sử dụng Groq API"""
    try:
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
        
        prompt = f"""Bạn là một dịch giả chuyên nghiệp. Hãy dịch đoạn văn bản sau từ {source_lang} sang {target_lang}.
        
        Yêu cầu dịch thuật:
        1. Điều chỉnh xuống dòng hợp lý
        2. Đảm bảo tính chính xác và tự nhiên trong ngôn ngữ đích
        3. Giữ nguyên các thuật ngữ chuyên môn hoặc tên riêng
        4. Duy trì giọng văn và phong cách của văn bản gốc
        
        Văn bản cần dịch:
        {content}
        """
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Lỗi khi dịch nội dung: {str(e)}"

def main():
    print("Chào mừng bạn đến với File Translator!")
    input_file = input("Nhập đường dẫn file cần dịch: ")
    output_file = input("Nhập đường dẫn file kết quả: ")
    source_lang = input("Nhập ngôn ngữ nguồn (ví dụ: Tiếng Anh): ")
    target_lang = input("Nhập ngôn ngữ đích (ví dụ: Tiếng Việt): ")
    
    print("\nĐang đọc file...")
    content = read_file(input_file)
    
    if isinstance(content, str) and not content.startswith("Lỗi"):
        print("Đang chia nhỏ nội dung...")
        chunks = split_text(content)
        
        print("Đang dịch...")
        translated_chunks = []
        total_chunks = len(chunks)
        
        for i, chunk in enumerate(chunks, 1):
            print(f"Đang dịch phần {i}/{total_chunks}...")
            translated_chunk = translate_content(chunk, source_lang, target_lang)
            translated_chunks.append(translated_chunk)
        
        final_translation = "\n".join(translated_chunks)
        
        print("Đang lưu kết quả...")
        if write_file(final_translation, output_file):
            print(f"\nDịch thành công! Kết quả đã được lưu vào: {output_file}")
        else:
            print("Có lỗi khi lưu file kết quả.")
    else:
        print(content)

if __name__ == "__main__":
    main()
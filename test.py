import tiktoken

def split_text_into_chunks(text, max_tokens=512):
    # Sử dụng mã hóa GPT-2 của OpenAI
    enc = tiktoken.get_encoding("gpt2")
    tokens = enc.encode(text)  # Mã hóa văn bản thành danh sách token
    
    # Chia danh sách token thành các phần nhỏ hơn
    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    
    # Giải mã các phần token trở lại thành văn bản
    return [enc.decode(chunk) for chunk in chunks]

# Ví dụ sử dụng
text = "Đây là một ví dụ về cách chia văn bản thành các phần nhỏ hơn. Văn bản này có thể dài hơn giới hạn token của GPT-3.5."
chunks = split_text_into_chunks(text, max_tokens=10)
for chunk in chunks:
    print(chunk)

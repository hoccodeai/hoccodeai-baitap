# Bài tập

Hiện tại, chúng ta đang hardcode câu hỏi vào biến `question` trong code. Do đó, nó chỉ chạy 1 lần rồi ngừng.

Các bạn có thể biến nó thành 1 app hoàn chỉnh bằng các bước sau:

1. Bỏ tất cả vào vòng lặp while True.
2. Sau đó đọc câu hỏi từ phía người dùng bằng hàm `input` của Python `question = input("Có câu hỏi gì về không bạn ơi: ")`
3. Lần lượt add câu hỏi của người dùng và câu trả lời của bot vào `messages` để bot nhớ ngữ cảnh
4. Có thể update system prompt để LLM trả lời hài hước và vui tính hơn.

Bạn sẽ làm ra được con bot như hình dưới.

![demo](https://assets.hoccodeai.com/03.1-LLM-advanced/01-function-calling/imgs/stock-demo.webp)

# Nội dung nộp bài

Viết và nộp file `chatbot.py`, hoặc để link Colab cũng được.
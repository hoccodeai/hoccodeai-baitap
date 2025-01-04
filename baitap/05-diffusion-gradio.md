# Đề bài

> Bài 4-6 là bonus, nếu bạn không thích tạo ảnh, có thể bỏ qua để làm bài 7

Dựa theo code ứng dụng tạo ảnh Gradio đã có

- Đổi model đang dùng sang khác để tạo ảnh anime/2.5D trên civitAI thay vì dùng model SD1.5 gốc
- Tạo 1 dropbox để chọn model giống như Stable Diffusion WebUI, thay vì hardcode như trên
- Thêm 1 số parameters khác như `seed`, `num_inference_steps`, `guidance_scale` vào giao diện để người dùng có thể tinh chỉnh hơn


# Nội dung nộp bài

Viết và nộp file `diffusion-gradio.py`, hoặc để link Colab cũng được.
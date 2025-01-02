import tkinter as tk
from tkinter import messagebox
import asyncio
import edge_tts

# Hàm chuyển văn bản thành giọng nói
async def text_to_speech(text, voice_name, output_file):
    try:
        communicator = edge_tts.Communicate(text, voice_name)
        await communicator.save(output_file)
        messagebox.showinfo("Thông báo", f"Đã lưu giọng nói vào file {output_file}")
    except edge_tts.exceptions.NoAudioReceived:
        messagebox.showerror("Lỗi", "Không nhận được âm thanh. Kiểm tra lại tham số.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# Hàm xử lý sự kiện khi người dùng nhấn nút "Chuyển đổi"
def on_convert_button_click():
    text = text_input.get("1.0", "end-1c")  # Lấy văn bản người dùng nhập
    if not text.strip():  # Kiểm tra nếu văn bản trống
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản.")
        return
    
    voice_name = voice_choice.get()  # Lấy giọng nói đã chọn
    output_file = "output_audio.mp3"  # Đặt tên tệp đầu ra

    # Chạy hàm chuyển văn bản thành giọng nói
    asyncio.run(text_to_speech(text, voice_name, output_file))

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Chuyển Văn Bản Thành Giọng Nói")

# Thêm label hướng dẫn
label = tk.Label(root, text="Nhập văn bản:")
label.pack(pady=10)

# Text box để nhập văn bản
text_input = tk.Text(root, height=10, width=40)
text_input.pack(pady=5)

# Thêm label cho việc chọn giọng nói
voice_label = tk.Label(root, text="Chọn giọng nói:")
voice_label.pack(pady=5)

# Combo box để chọn giọng nói (Nam hoặc Nữ)
voice_choice = tk.StringVar()
voice_choice.set("vi-VN-HoaiMyNeural")  # Giọng nữ mặc định
voice_menu = tk.OptionMenu(root, voice_choice, "vi-VN-HoaiMyNeural", "vi-VN-NamMinhNeural")
voice_menu.pack(pady=5)

# Nút "Chuyển đổi" để bắt đầu quá trình chuyển văn bản thành giọng nói
convert_button = tk.Button(root, text="Chuyển đổi", command=on_convert_button_click)
convert_button.pack(pady=20)

# Chạy vòng lặp chính của Tkinter
root.mainloop()

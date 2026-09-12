"""
=============================================================================
BÀI 3: CÁC LUỒNG VÀO/RA TIÊU CHUẨN (sys.stdin, sys.stdout, sys.stderr)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- Trong hệ điều hành, mọi tiến trình mặc định đều có 3 luồng dữ liệu (Streams):
  1. `sys.stdin` (Standard Input - File descriptor 0): Luồng nhận dữ liệu đầu vào.
     Hàm `input()` trong Python bản chất là đọc từ `sys.stdin`.
  2. `sys.stdout` (Standard Output - File descriptor 1): Luồng xuất dữ liệu chuẩn.
     Hàm `print()` trong Python bản chất là ghi ra `sys.stdout`.
  3. `sys.stderr` (Standard Error - File descriptor 2): Luồng ghi nhận thông báo lỗi riêng biệt.
     Ngay cả khi `stdout` bị chuyển hướng vào file, `stderr` vẫn hiển thị trực tiếp lên màn hình console!

💡 TRƯỜNG HỢP SỬ DỤNG:
- Chuyển hướng toàn bộ output của chương trình ra file log mà không cần sửa từng lệnh `print()`.
- Tách biệt log kết quả và log cảnh báo/lỗi (Best Practice trong hệ thống Linux/Server).
- Đọc dữ liệu dạng đường ống (Piping data: `cat data.txt | python process.py`).
=============================================================================
"""

import sys
import io

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def demo_direct_stream_writing():
    """Ghi trực tiếp vào stdout và stderr"""
    print("--- 1. Ghi Trực Tiếp Vào stdout và stderr ---")
    
    # Ghi ra stdout (tương đương print nhưng không tự động xuống dòng)
    sys.stdout.write("Đây là thông điệp bình thường ghi qua sys.stdout\n")
    sys.stdout.flush() # Đẩy dữ liệu ra màn hình ngay lập tức

    # Ghi ra stderr (thường dùng cho thông báo lỗi, cảnh báo)
    sys.stderr.write("⚠️ [ERROR LOG] Đây là thông điệp cảnh báo ghi qua sys.stderr\n")
    sys.stderr.flush()

def demo_stdout_redirection():
    """Chuyển hướng sys.stdout vào bộ đệm tạm thời (StringIO) hoặc file"""
    print("\n--- 2. Chuyển Hướng sys.stdout (Output Redirection) ---")
    
    # Lưu lại stdout gốc của hệ thống để khôi phục sau này
    original_stdout = sys.stdout
    
    # Tạo một bộ nhớ đệm giả lập luồng ghi
    captured_output = io.StringIO()
    
    # Chuyển hướng stdout sang bộ nhớ đệm
    sys.stdout = captured_output
    
    # Các lệnh print bây giờ sẽ ghi vào captured_output chứ không hiện ra màn hình!
    print("Dòng 1: Dữ liệu đang được ghi âm thầm...")
    print("Dòng 2: Phép tính 20 * 5 =", 20 * 5)
    print("Dòng 3: Hoàn thành tác vụ ngầm.")
    
    # Khôi phục lại stdout gốc để in ra màn hình bình thường
    sys.stdout = original_stdout
    if sys.platform.startswith("win"):
        sys.stdout.reconfigure(encoding="utf-8")
    
    print("✅ Đã khôi phục stdout gốc.")
    print("Dữ liệu đã thu thập được từ bộ đệm:")
    print("-" * 40)
    print(captured_output.getvalue().strip())
    print("-" * 40)

if __name__ == "__main__":
    demo_direct_stream_writing()
    demo_stdout_redirection()

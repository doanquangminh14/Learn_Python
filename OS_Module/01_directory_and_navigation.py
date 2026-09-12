"""
=============================================================================
BÀI 1: ĐIỀU HƯỚNG VÀ QUẢN LÝ THƯ MỤC TRONG OS MODULE
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `os.getcwd()`: (Get Current Working Directory) Trả về đường dẫn thư mục làm việc hiện tại của tiến trình.
- `os.chdir(path)`: Thay đổi thư mục làm việc hiện tại sang một vị trí mới.
- `os.listdir(path='.')`: Trả về danh sách tất cả các tên tệp và thư mục con nằm trong thư mục chỉ định.
- `os.mkdir(path)`: Tạo một thư mục đơn lẻ (báo lỗi nếu thư mục cha chưa tồn tại).
- `os.makedirs(path, exist_ok=True)`: Tạo cây thư mục lồng nhau (tự động tạo toàn bộ các thư mục cha bị thiếu). Tham số `exist_ok=True` ngăn chặn lỗi nếu thư mục đã có sẵn.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Tự động tạo thư mục lưu kết quả (`logs/2026/09/`) trước khi ghi file.
- Liệt kê và xử lý hàng loạt file trong một thư mục đầu vào.
=============================================================================
"""

import os
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. ĐIỀU HƯỚNG VÀ KIỂM TRA THƯ MỤC HIỆN TẠI")
    print("=" * 60)

    # 1. Lấy thư mục hiện tại
    cwd = os.getcwd()
    print(f"Thư mục làm việc hiện tại (os.getcwd): \n-> {cwd}\n")

    # 2. Liệt kê các file/folder trong thư mục hiện tại
    entries = os.listdir(".")
    print(f"Danh sách các mục trong thư mục hiện tại ({len(entries)} mục):")
    for item in sorted(entries)[:8]: # Hiển thị 8 mục đầu
        print(f" - {item}")

    print("\n" + "=" * 60)
    print("2. TẠO THƯ MỤC ĐƠN VÀ THƯ MỤC LỒNG NHAU (mkdir & makedirs)")
    print("=" * 60)

    # Đường dẫn demo
    demo_single_dir = "os_demo_single"
    demo_nested_dir = "os_demo_parent/sub_dir_1/sub_dir_2"

    # Tạo thư mục đơn
    if not os.path.exists(demo_single_dir):
        os.mkdir(demo_single_dir)
        print(f"✅ Đã tạo thư mục đơn: {demo_single_dir}")
    else:
        print(f"ℹ️ Thư mục đơn '{demo_single_dir}' đã tồn tại.")

    # Tạo cây thư mục lồng nhau an toàn với makedirs
    os.makedirs(demo_nested_dir, exist_ok=True)
    print(f"✅ Đã tạo cây thư mục lồng nhau an toàn: {demo_nested_dir}")

    # Dọn dẹp thư mục demo sau khi thực hành
    os.removedirs(demo_nested_dir)
    if os.path.exists(demo_single_dir):
        os.rmdir(demo_single_dir)
    print("🧹 Đã dọn dẹp sạch sẽ các thư mục demo!")

if __name__ == "__main__":
    main()

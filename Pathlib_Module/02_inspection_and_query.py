"""
=============================================================================
BÀI 2: KIỂM TRA TRẠNG THÁI VÀ TRUY VẤN METADATA (Inspection & Query)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `Path.cwd()`: Lấy thư mục làm việc hiện tại (tương đương `os.getcwd()`).
- `Path.home()`: Lấy thư mục người dùng cá nhân (ví dụ: `C:/Users/Minh Doan`).
- `.exists()`: Kiểm tra đường dẫn có tồn tại thực sự trên đĩa cứng hay không.
- `.is_file()` & `.is_dir()`: Kiểm tra loại tệp tin hay thư mục.
- `.is_absolute()`: Kiểm tra đường dẫn có phải là tuyệt đối hay không.
- `.resolve()`: Chuyển đổi đường dẫn tương đối thành tuyệt đối, loại bỏ các ký tự `..` hoặc `.` và giải quyết các Symbolic Links (Symlink).
- `.stat()`: Lấy thông tin kích thước `st_size` và thời gian sửa đổi `st_mtime`.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Kiểm tra tính hợp lệ của file đầu vào trước khi bắt đầu xử lý.
- Chuẩn hóa đường dẫn cấu hình dự án.
=============================================================================
"""

from pathlib import Path
import time
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. CÁC HÀM TRUY VẤN HỆ THỐNG CƠ BẢN")
    print("=" * 60)

    current_dir = Path.cwd()
    user_home = Path.home()

    print(f"Thư mục làm việc hiện tại (Path.cwd): \n-> {current_dir}")
    print(f"Thư mục cá nhân (Path.home):         \n-> {user_home}")

    print("\n" + "=" * 60)
    print("2. KIỂM TRA TỒN TẠI VÀ CHUẨN HÓA ĐƯỜNG DẪN")
    print("=" * 60)

    # Đường dẫn tương đối
    rel_path = Path("notebook/data/customer_orders_raw.csv")

    print(f"Đường dẫn kiểm tra: '{rel_path}'")
    print(f" - Có tồn tại không? (.exists()):    {rel_path.exists()}")
    print(f" - Có phải là file? (.is_file()):     {rel_path.is_file()}")
    print(f" - Có phải thư mục? (.is_dir()):     {rel_path.is_dir()}")
    print(f" - Là đường dẫn tuyệt đối?           {rel_path.is_absolute()}")

    # Chuyển thành đường dẫn tuyệt đối chuẩn hóa
    resolved_path = rel_path.resolve()
    print(f"\nĐường dẫn tuyệt đối (.resolve()):\n-> {resolved_path}")

    # Đọc Metadata
    if rel_path.exists():
        stat_info = rel_path.stat()
        print(f"\nThông tin kích thước file:")
        print(f" - Dung lượng:      {stat_info.st_size} bytes")
        print(f" - Sửa đổi lần cuối: {time.ctime(stat_info.st_mtime)}")

if __name__ == "__main__":
    main()

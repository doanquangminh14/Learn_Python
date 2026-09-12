"""
=============================================================================
BÀI 1: KHỞI TẠO ĐƯỜNG DẪN VÀ BÓC TÁCH CÁC THÀNH PHẦN (Path Creation & Parts)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `Path(*pathsegments)`: Tạo một đối tượng đường dẫn độc lập với hệ điều hành.
- **Toán tử `/` (Slash Operator)**: Cho phép ghép nối các thành phần đường dẫn một cách tự nhiên và trực quan như viết phép chia trong toán.
- Các thuộc tính bóc tách thành phần:
  - `.name`: Tên file đầy đủ kèm đuôi mở rộng (ví dụ: `report_2026.csv`).
  - `.stem`: Tên file gốc không kèm đuôi mở rộng (ví dụ: `report_2026`).
  - `.suffix`: Đuôi mở rộng của file (ví dụ: `.csv`).
  - `.suffixes`: Danh sách tất cả các đuôi (ví dụ: `.tar.gz` -> `['.tar', '.gz']`).
  - `.parent`: Đường dẫn thư mục cha trực tiếp chứa file.
  - `.parents`: Danh sách tất cả các thư mục tổ tiên theo cấp bậc.
  - `.parts`: Tuple chứa tất cả các thành phần đường dẫn riêng lẻ.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Đổi đuôi file (`.with_suffix('.pdf')`), đổi tên file (`.with_name('new_name.txt')`).
=============================================================================
"""

from pathlib import Path
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. KHỞI TẠO ĐƯỜNG DẪN VỚI TOÁN TỬ /")
    print("=" * 60)

    # Ghép nối đường dẫn với toán tử /
    base_folder = Path("my_project")
    sub_folder = "assets"
    file_path = base_folder / sub_folder / "archive.tar.gz"

    print(f"Đường dẫn đã tạo: {file_path}")
    print(f"Kiểu dữ liệu:     {type(file_path)}")

    print("\n" + "=" * 60)
    print("2. BÓC TÁCH CÁC THUỘC TÍNH CỦA ĐƯỜNG DẪN")
    print("=" * 60)

    sample_path = Path("C:/Users/Minh Doan/Projects/sales_report_2026.xlsx")

    print(f"Đường dẫn mẫu: {sample_path}")
    print(f" - .name (Tên đầy đủ):            {sample_path.name}")
    print(f" - .stem (Tên không đuôi):        {sample_path.stem}")
    print(f" - .suffix (Đuôi mở rộng):        {sample_path.suffix}")
    print(f" - .parent (Thư mục cha):         {sample_path.parent}")
    print(f" - .drive (Ổ đĩa trên Windows):   {sample_path.drive}")
    print(f" - .parts (Tất cả thành phần):    {sample_path.parts}")

    print("\n" + "=" * 60)
    print("3. BIẾN ĐỔI ĐƯỜNG DẪN DỄ DÀNG (with_suffix & with_name)")
    print("=" * 60)

    # Đổi đuôi từ .xlsx sang .csv
    csv_path = sample_path.with_suffix(".csv")
    print(f"Đổi đuôi file (with_suffix):      {csv_path.name}")

    # Đổi tên file giữ nguyên thư mục cha
    backup_path = sample_path.with_name("sales_backup.xlsx")
    print(f"Đổi tên file (with_name):        {backup_path}")

if __name__ == "__main__":
    main()

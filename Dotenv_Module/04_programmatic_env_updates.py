"""
=============================================================================
BÀI 4: GHI, CẬP NHẬT VÀ XÓA BIẾN BẰNG CODE (PROGRAMMATIC UPDATES)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `set_key(dotenv_path, key_to_set, value_to_set, quote_mode="always")`:
  + Ghi hoặc cập nhật một cặp key-value trực tiếp vào file `.env` trên đĩa cứng mà vẫn giữ nguyên các comment hoặc cấu trúc file có sẵn.
- `get_key(dotenv_path, key_to_get)`:
  + Lấy giá trị của một key cụ thể từ file `.env` mà không cần nạp cả file vào môi trường.
- `unset_key(dotenv_path, key_to_unset)`:
  + Xóa một biến ra khỏi file `.env`.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Xây dựng CLI Tools/Setup Wizard (hỏi thông tin cấu hình của người dùng khi cài đặt rồi lưu vào `.env`).
- Tự động lưu Access Token/Refresh Token mới sau khi refresh OAuth2.
=============================================================================
"""

import os
import sys
from dotenv import set_key, get_key, unset_key

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. KHỞI TẠO FILE .env BAN ĐẦU")
    print("=" * 60)

    demo_file = "demo_mutate.env"
    with open(demo_file, "w", encoding="utf-8") as f:
        f.write("# Cấu hình xác thực\n")
        f.write("ACCESS_TOKEN=initial_old_token\n")
        f.write("REFRESH_COUNT=0\n")

    print(f"Đọc ACCESS_TOKEN ban đầu: {get_key(demo_file, 'ACCESS_TOKEN')}")

    print("\n" + "=" * 60)
    print("2. CẬP NHẬT VÀ THÊM MỚI BIẾN VỚI set_key")
    print("=" * 60)

    # 1. Cập nhật key đã tồn tại
    set_key(demo_file, "ACCESS_TOKEN", "new_jwt_token_2026_xyz")
    # 2. Thêm key hoàn toàn mới
    set_key(demo_file, "LAST_UPDATED", "2026-09-13T16:45:00Z")

    print("📄 Nội dung file sau khi set_key:")
    with open(demo_file, "r", encoding="utf-8") as f:
        print(f.read().strip())

    print("\n" + "=" * 60)
    print("3. XÓA BIẾN VỚI unset_key")
    print("=" * 60)

    # Xóa key REFRESH_COUNT
    unset_key(demo_file, "REFRESH_COUNT")

    print("📄 Nội dung file sau khi unset_key:")
    with open(demo_file, "r", encoding="utf-8") as f:
        print(f.read().strip())

    # Dọn dẹp file tạm
    if os.path.exists(demo_file):
        os.remove(demo_file)
    print("\n🧹 Đã dọn dẹp file demo!")

if __name__ == "__main__":
    main()

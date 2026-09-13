"""
=============================================================================
BÀI 1: NẠP VÀ ĐỌC BIẾN MÔI TRƯỜNG VỚI `load_dotenv` VÀ `os.getenv`
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `load_dotenv(dotenv_path=None, override=False)`:
  + Tìm kiếm và nạp các cặp key-value từ file `.env` vào biến môi trường hệ thống (`os.environ`).
  + Nếu không truyền `dotenv_path`, hàm sẽ tự tìm file `.env` trong thư mục hiện tại hoặc các thư mục cha (`find_dotenv()`).
- `os.getenv(key, default=None)`:
  + Lấy giá trị của biến môi trường.
  + Nếu biến không tồn tại, trả về giá trị mặc định `default` thay vì gây lỗi.

💡 LƯU Ý QUAN TRỌNG:
- Mọi giá trị đọc từ `os.getenv()` đều có kiểu dữ liệu là `str` (String).
- Bạn cần tự ép kiểu (Type Casting) sang `int`, `float`, hoặc `bool` khi sử dụng cho cổng port, cờ debug, v.v.
=============================================================================
"""

import os
import sys
from dotenv import load_dotenv, find_dotenv

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. TÌM KIẾM VÀ NẠP FILE .env TỰ ĐỘNG")
    print("=" * 60)

    # Tạo một file .env mẫu tạm thời phục vụ demo
    demo_env_file = "demo_basic.env"
    with open(demo_env_file, "w", encoding="utf-8") as f:
        f.write("APP_TITLE=Python Learning Hub\n")
        f.write("SERVER_PORT=8080\n")
        f.write("DEBUG_MODE=true\n")
        f.write("DATABASE_TIMEOUT=5.5\n")
        f.write("SECRET_KEY=super_secret_xyz123\n")

    # Nạp file .env chỉ định
    loaded = load_dotenv(dotenv_path=demo_env_file)
    print(f"Trạng thái nạp file '{demo_env_file}': {'✅ Thành công' if loaded else '❌ Thất bại'}\n")

    print("=" * 60)
    print("2. ĐỌC BIẾN VÀ ÉP KIỂU DỮ LIỆU (TYPE CASTING)")
    print("=" * 60)

    # 1. Đọc kiểu chuỗi (String)
    app_title = os.getenv("APP_TITLE", "Default App")
    print(f"🔹 App Title (str): {app_title}")

    # 2. Ép kiểu số nguyên (Integer)
    port_raw = os.getenv("SERVER_PORT", "3000")
    server_port = int(port_raw)
    print(f"🔹 Server Port (int): {server_port} (Kiểu: {type(server_port).__name__})")

    # 3. Ép kiểu số thực (Float)
    timeout_raw = os.getenv("DATABASE_TIMEOUT", "10.0")
    db_timeout = float(timeout_raw)
    print(f"🔹 DB Timeout (float): {db_timeout}s (Kiểu: {type(db_timeout).__name__})")

    # 4. Ép kiểu Boolean chuẩn xác
    # Lưu ý: bool("False") trong Python là True! Cần so sánh chuỗi:
    debug_raw = os.getenv("DEBUG_MODE", "false").strip().lower()
    is_debug = debug_raw in ("true", "1", "yes", "t")
    print(f"🔹 Debug Mode (bool): {is_debug} (Kiểu: {type(is_debug).__name__})")

    # 5. Đọc biến không tồn tại với giá trị dự phòng (Fallback / Default)
    redis_host = os.getenv("REDIS_HOST", "127.0.0.1")
    print(f"🔹 Redis Host (Default): {redis_host}")

    # Dọn dẹp file tạm
    if os.path.exists(demo_env_file):
        os.remove(demo_env_file)
    print("\n🧹 Đã dọn dẹp file demo thành công!")

if __name__ == "__main__":
    main()

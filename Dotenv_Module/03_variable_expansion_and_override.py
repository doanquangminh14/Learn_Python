"""
=============================================================================
BÀI 3: MỞ RỘNG BIẾN (VARIABLE EXPANSION) VÀ GHI ĐÈ (OVERRIDE)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
1. **Variable Expansion (Nội suy biến)**:
   - Cho phép biến này tham chiếu đến giá trị của biến khác trong file `.env` bằng cú pháp `${VAR_NAME}` hoặc `$VAR_NAME`.
   - Ví dụ:
     `BASE_URL=https://api.example.com`
     `USER_ENDPOINT=${BASE_URL}/v1/users`

2. **Cơ chế Ghi đè (Override)**:
   - Mặc định `load_dotenv(override=False)`: Nếu một biến đã tồn tại sẵn trong hệ điều hành (hoặc từ container Docker/CI-CD), `load_dotenv` sẽ KHÔNG ghi đè.
   - Khi đặt `override=True`: Giá trị trong file `.env` sẽ buộc phải ghi đè giá trị hiện tại của hệ thống.
=============================================================================
"""

import os
import sys
from dotenv import load_dotenv

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. MỞ RỘNG BIẾN (VARIABLE EXPANSION / INTERPOLATION)")
    print("=" * 60)

    demo_expand_file = "demo_expand.env"
    with open(demo_expand_file, "w", encoding="utf-8") as f:
        f.write("PROTOCOL=https\n")
        f.write("DOMAIN=api.github.com\n")
        f.write("API_VERSION=v3\n")
        # Sử dụng nội suy biến ${PROTOCOL}, ${DOMAIN}, ${API_VERSION}
        f.write("FULL_API_URL=${PROTOCOL}://${DOMAIN}/${API_VERSION}\n")
        f.write("GRAPHQL_URL=${FULL_API_URL}/graphql\n")

    load_dotenv(demo_expand_file, override=True)

    print(f"🔹 FULL_API_URL: {os.getenv('FULL_API_URL')}")
    print(f"🔹 GRAPHQL_URL : {os.getenv('GRAPHQL_URL')}")

    print("\n" + "=" * 60)
    print("2. CƠ CHẾ GHI ĐÈ: override=False VS override=True")
    print("=" * 60)

    # Giả lập biến hệ thống đã tồn tại từ trước
    os.environ["APP_MODE"] = "PRODUCTION_SERVER"
    print(f"1️⃣ Giá trị ban đầu trong os.environ: {os.getenv('APP_MODE')}")

    demo_override_file = "demo_override.env"
    with open(demo_override_file, "w", encoding="utf-8") as f:
        f.write("APP_MODE=DEVELOPMENT_LOCAL\n")

    # Mặc định override=False -> Giữ nguyên giá trị của hệ thống
    load_dotenv(demo_override_file, override=False)
    print(f"2️⃣ Sau khi load với override=False: {os.getenv('APP_MODE')} (Không bị đè)")

    # Bật override=True -> File .env thắng
    load_dotenv(demo_override_file, override=True)
    print(f"3️⃣ Sau khi load với override=True : {os.getenv('APP_MODE')} (Đã bị đè bởi file .env)")

    # Dọn dẹp file tạm
    for tmp in (demo_expand_file, demo_override_file):
        if os.path.exists(tmp):
            os.remove(tmp)
    print("\n🧹 Đã dọn dẹp các file demo!")

if __name__ == "__main__":
    main()

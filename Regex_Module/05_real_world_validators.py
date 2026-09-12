"""
=============================================================================
BÀI 5: BỘ HÀM VALIDATOR DỮ LIỆU THỰC TẾ TRONG DỰ ÁN (Real-World Regex Validators)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- Sử dụng `re.compile()` để tiền biên dịch các mẫu Regex phổ biến giúp tối ưu tốc độ.
- Kết hợp `re.fullmatch()` để đảm bảo toàn bộ chuỗi khớp 100% không có ký tự rác.
- Xây dựng các hàm kiểm tra logic thực tế:
  1. Email hợp lệ (RFC 5322 cơ bản).
  2. Số điện thoại di động Việt Nam (10 chữ số, bắt đầu bằng các đầu số chuẩn 03, 05, 07, 08, 09).
  3. Mật khẩu mạnh (Tối thiểu 8 ký tự, có chữ hoa, chữ thường, số và ký tự đặc biệt).
  4. Địa chỉ IPv4 hợp lệ (4 octet từ 0-255).
  5. URL / Link trang web.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Tích hợp vào Form Đăng ký / Đăng nhập, API Validation middleware.
=============================================================================
"""

import re
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

class DataValidator:
    # 1. Regex Email
    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    
    # 2. Regex Số điện thoại Việt Nam (Đầu số: 03, 05, 07, 08, 09 + 8 số)
    VIETNAM_PHONE_REGEX = re.compile(r"^(0|\+84)(3[2-9]|5[2689]|7[06-9]|8[1-9]|9[0-9])\d{7}$")
    
    # 3. Regex Mật khẩu mạnh: >= 8 ký tự, ít nhất 1 hoa, 1 thường, 1 số, 1 ký tự đặc biệt
    STRONG_PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    
    # 4. Regex Địa chỉ IPv4
    IPV4_REGEX = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    
    # 5. Regex Website URL
    URL_REGEX = re.compile(r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(\/[a-zA-Z0-9-._~:?#[\]@!$&'()*+,;=]*)?$")

    @classmethod
    def is_valid_email(cls, email: str) -> bool:
        return bool(cls.EMAIL_REGEX.fullmatch(email.strip()))

    @classmethod
    def is_valid_vn_phone(cls, phone: str) -> bool:
        # Xóa khoảng trắng, dấu gạch ngang
        clean_phone = re.sub(r"[\s.-]", "", phone)
        return bool(cls.VIETNAM_PHONE_REGEX.fullmatch(clean_phone))

    @classmethod
    def is_strong_password(cls, password: str) -> bool:
        return bool(cls.STRONG_PASSWORD_REGEX.fullmatch(password))

    @classmethod
    def is_valid_ipv4(cls, ip: str) -> bool:
        return bool(cls.IPV4_REGEX.fullmatch(ip.strip()))

    @classmethod
    def is_valid_url(cls, url: str) -> bool:
        return bool(cls.URL_REGEX.fullmatch(url.strip()))

def main():
    print("=" * 60)
    print("KIỂM TRA BỘ HÀM VALIDATOR THỰC TẾ")
    print("=" * 60)

    # 1. Kiểm tra Email
    emails = ["minh.doan@tech.io", "invalid_email@", "user@domain.com.vn"]
    print("\n1. 📧 Kiểm tra Email:")
    for e in emails:
        print(f"   * '{e}': {'✅ Hợp lệ' if DataValidator.is_valid_email(e) else '❌ Không hợp lệ'}")

    # 2. Kiểm tra Số điện thoại Việt Nam
    phones = ["0901234567", "+84987654321", "0123456789", "090-123-4567"]
    print("\n2. 📱 Kiểm tra Số điện thoại Việt Nam:")
    for p in phones:
        print(f"   * '{p}': {'✅ Hợp lệ' if DataValidator.is_valid_vn_phone(p) else '❌ Không hợp lệ'}")

    # 3. Kiểm tra Mật khẩu mạnh
    passwords = ["123456", "Pass123", "P@ssw0rd2026", "Weakpass@"]
    print("\n3. 🔐 Kiểm tra Mật khẩu mạnh:")
    for pwd in passwords:
        print(f"   * '{pwd}': {'✅ Mạnh' if DataValidator.is_strong_password(pwd) else '❌ Yếu'}")

    # 4. Kiểm tra IPv4
    ips = ["192.168.1.1", "256.0.0.1", "10.0.0.255", "invalid.ip"]
    print("\n4. 🌐 Kiểm tra Địa chỉ IPv4:")
    for ip in ips:
        print(f"   * '{ip}': {'✅ Hợp lệ' if DataValidator.is_valid_ipv4(ip) else '❌ Không hợp lệ'}")

if __name__ == "__main__":
    main()

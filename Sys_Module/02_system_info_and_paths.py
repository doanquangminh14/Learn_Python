"""
=============================================================================
BÀI 2: THÔNG TIN HỆ THỐNG & CƠ CHẾ TÌM KIẾM MODULE (sys.path & sys.platform)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `sys.version` & `sys.version_info`: Chứa thông tin phiên bản Python hiện tại.
- `sys.platform`: Xác định hệ điều hành (win32, linux, darwin/macOS).
- `sys.executable`: Đường dẫn tuyệt đối tới file thực thi python.exe đang chạy.
- `sys.path`: Danh sách các đường dẫn thư mục mà Python sẽ duyệt qua theo thứ tự
  để tìm file khi bạn gọi lệnh `import module_name`.
  Thứ tự ưu tiên:
  1. Thư mục chứa script đang chạy (hoặc thư mục hiện tại).
  2. Các thư mục trong biến môi trường PYTHONPATH (nếu có).
  3. Thư mục cài đặt chuẩn của Python (Standard Library & site-packages).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Kiểm tra phiên bản Python tối thiểu trước khi chạy app (tránh lỗi cú pháp phiên bản cũ).
- Viết code đa nền tảng (chạy khác nhau trên Windows và Linux/macOS).
- Thêm đường dẫn thư mục cha/con vào `sys.path` để import module tự viết không bị lỗi `ModuleNotFoundError`.
=============================================================================
"""

import sys
import os

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def check_python_version(min_major=3, min_minor=10):
    """Kiểm tra phiên bản Python hiện tại có đáp ứng yêu cầu tối thiểu không"""
    current_major = sys.version_info.major
    current_minor = sys.version_info.minor
    
    print(f"Phiên bản Python hiện tại: {sys.version.split()[0]}")
    print(f"Chi tiết sys.version_info: {sys.version_info}")
    
    if (current_major, current_minor) < (min_major, min_minor):
        print(f"❌ Cảnh báo: Ứng dụng yêu cầu tối thiểu Python {min_major}.{min_minor}+")
        return False
    print(f"✅ Phiên bản Python đạt yêu cầu (>= {min_major}.{min_minor})")
    return True

def inspect_platform():
    """Kiểm tra hệ điều hành"""
    platform_name = sys.platform
    print(f"\nHệ điều hành hiện tại (sys.platform): {platform_name}")
    
    if platform_name.startswith("win"):
        print("-> Đang chạy trên môi trường Windows")
    elif platform_name.startswith("linux"):
        print("-> Đang chạy trên môi trường Linux")
    elif platform_name.startswith("darwin"):
        print("-> Đang chạy trên môi trường macOS")
    else:
        print(f"-> Môi trường khác: {platform_name}")

    print(f"Đường dẫn trình thực thi Python: {sys.executable}")

def demonstrate_sys_path():
    """Khám phá và tùy biến sys.path"""
    print("\n" + "=" * 60)
    print("DANH SÁCH ĐƯỜNG DẪN TÌM KIẾM MODULE (sys.path)")
    print("=" * 60)
    
    for idx, path in enumerate(sys.path, start=1):
        print(f"[{idx}] {path}")

    # Kỹ thuật quan trọng: Thêm đường dẫn thư mục tùy chỉnh vào sys.path
    custom_dir = os.path.abspath("./custom_modules")
    if custom_dir not in sys.path:
        sys.path.append(custom_dir)
        print(f"\n✅ Đã thêm thư mục tùy chỉnh vào sys.path: {custom_dir}")
        print(f"Tổng số đường dẫn hiện tại: {len(sys.path)}")

if __name__ == "__main__":
    check_python_version()
    inspect_platform()
    demonstrate_sys_path()

"""
=============================================================================
BÀI 4: QUẢN LÝ CẤU HÌNH VÀ BẮT LỖI JSONDecodeError AN TOÀN
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- Khi đọc file JSON bị lỗi cú pháp (thừa dấu phẩy `,`, thiếu dấu ngoặc `}`, dùng nháy đơn `'` thay vì nháy kép `"`), Python sẽ ném ngoại lệ `json.JSONDecodeError`.
- Ngoại lệ này chứa các thuộc tính quan trọng:
  - `e.msg`: Nội dung thông báo lỗi.
  - `e.lineno`: Dòng xảy ra lỗi.
  - `e.colno`: Cột xảy ra lỗi.
  - `e.pos`: Vị trí ký tự trong chuỗi.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Xây dựng lớp `ConfigManager` tự động tạo file cài đặt mặc định nếu file chưa có hoặc bị hỏng.
- Kiểm tra tính toàn vẹn của file cấu hình khi khởi động ứng dụng Web/Server.
=============================================================================
"""

import json
import os
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

class ConfigManager:
    """Quản lý file cấu hình JSON an toàn với cơ chế Fallback"""
    
    DEFAULT_CONFIG = {
        "app_name": "MyPythonApp",
        "version": "1.0.0",
        "debug_mode": True,
        "database": {
            "host": "localhost",
            "port": 5432,
            "timeout": 30
        },
        "theme": "dark"
    }

    def __init__(self, config_filepath="app_config.json"):
        self.config_filepath = config_filepath
        self.config = self.load_config()

    def load_config(self):
        """Tải cấu hình từ file, nếu không tồn tại hoặc lỗi thì tự tạo mặc định"""
        if not os.path.exists(self.config_filepath):
            print(f"ℹ️ File '{self.config_filepath}' chưa tồn tại. Đang tạo cấu hình mặc định...")
            self.save_config(self.DEFAULT_CONFIG)
            return self.DEFAULT_CONFIG.copy()

        try:
            with open(self.config_filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(f"✅ Đã tải cấu hình thành công từ '{self.config_filepath}'")
                return data
        except json.JSONDecodeError as e:
            print(f"❌ [LỖI CÚ PHÁP JSON] File cấu hình '{self.config_filepath}' bị hỏng!")
            print(f"   - Chi tiết: {e.msg}")
            print(f"   - Tại dòng: {e.lineno}, Cột: {e.colno}")
            print("   -> Đang sử dụng cấu hình mặc định an toàn.")
            return self.DEFAULT_CONFIG.copy()
        except Exception as e:
            print(f"❌ Lỗi không xác định khi đọc config: {e}")
            return self.DEFAULT_CONFIG.copy()

    def save_config(self, config_data=None):
        """Lưu dữ liệu cấu hình ra file"""
        data_to_save = config_data or self.config
        with open(self.config_filepath, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)
        print(f"💾 Đã lưu cấu hình vào '{self.config_filepath}'")

def demo_corrupted_json_handling():
    """Demo bắt lỗi khi file JSON có cú pháp sai"""
    print("=" * 60)
    print("1. BẮT LỖI CÚ PHÁP JSON (JSONDecodeError)")
    print("=" * 60)

    # Chuỗi JSON bị lỗi (dùng dấu nháy đơn ' thay vì nháy kép ", thừa dấu phẩy)
    malformed_json_str = "{ 'name': 'Python', 'version': 3.13, }"

    try:
        json.loads(malformed_json_str)
    except json.JSONDecodeError as err:
        print(f"Phát hiện lỗi JSONDecodeError:")
        print(f" - Thông báo lỗi: {err.msg}")
        print(f" - Vị trí dòng:  {err.lineno}")
        print(f" - Vị trí cột:   {err.colno}")

def main():
    demo_corrupted_json_handling()

    print("\n" + "=" * 60)
    print("2. THỬ NGHIỆM ConfigManager")
    print("=" * 60)

    manager = ConfigManager("test_config.json")
    print(f"Cấu hình đang chạy: App '{manager.config['app_name']}', Cổng DB: {manager.config['database']['port']}")

    # Dọn dẹp file test
    if os.path.exists("test_config.json"):
        os.remove("test_config.json")
        print("🧹 Đã dọn dẹp file test_config.json!")

if __name__ == "__main__":
    main()

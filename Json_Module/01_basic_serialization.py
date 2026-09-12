"""
=============================================================================
BÀI 1: CHUYỂN ĐỔI CHUỖI JSON (json.dumps & json.loads)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `json.dumps(obj)`: (Dump String) Chuyển đổi đối tượng Python (dict, list) thành một chuỗi văn bản JSON (str).
  - `indent=4`: Tự động thụt lề định dạng JSON đẹp mắt (Pretty Print).
  - `sort_keys=True`: Sắp xếp các khóa (keys) theo thứ tự bảng chữ cái.
  - `ensure_ascii=False`: Giữ nguyên ký tự Unicode (tiếng Việt có dấu, emoji) thay vì bị escape thành `\u00e0...`.
- `json.loads(json_str)`: (Load String) Phân tích một chuỗi JSON (str) thành cấu trúc dữ liệu Python tương ứng (dict, list).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Nhận và gửi dữ liệu qua API HTTP (REST API payload).
- Tạo chuỗi JSON hiển thị trên console hoặc ghi vào hệ thống message queue (Kafka, RabbitMQ).
=============================================================================
"""

import json
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. PYTHON OBJECT SANG JSON STRING (json.dumps)")
    print("=" * 60)

    user_profile = {
        "user_id": 1007,
        "name": "Đoàn Quang Minh",
        "email": "minh.doan@example.com",
        "is_active": True,
        "skills": ["Python", "Pandas", "Machine Learning", "System Design"],
        "balance": 1500.75,
        "extra_info": None
    }

    # Chuyển đổi sang JSON String tiêu chuẩn (nén trên 1 dòng)
    compact_json = json.dumps(user_profile)
    print(f"JSON String nén (mặc định):\n{compact_json}\n")

    # Chuyển đổi sang JSON String đẹp mắt có thụt đầu dòng và hỗ trợ tiếng Việt
    pretty_json = json.dumps(
        user_profile,
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )
    print("JSON String định dạng đẹp mắt (indent=4, ensure_ascii=False):")
    print(pretty_json)

    print("\n" + "=" * 60)
    print("2. JSON STRING SANG PYTHON DICT (json.loads)")
    print("=" * 60)

    json_input = '''
    {
        "status": "success",
        "code": 200,
        "data": {
            "title": "Khóa Học Python Pro",
            "students_count": 1250,
            "rating": 4.95,
            "is_free": false
        }
    }
    '''

    # Parse chuỗi JSON thành Python Dictionary
    parsed_data = json.loads(json_input)
    print(f"Kiểu dữ liệu sau khi loads: {type(parsed_data)}")
    print(f"Mã phản hồi: {parsed_data['code']}")
    print(f"Tên khóa học: {parsed_data['data']['title']}")
    print(f"Đánh giá: {parsed_data['data']['rating']} ⭐")

if __name__ == "__main__":
    main()

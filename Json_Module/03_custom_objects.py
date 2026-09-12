"""
=============================================================================
BÀI 3: XỬ LÝ ĐỐI TƯỢNG TÙY CHỈNH (datetime, set, OOP Class) TRONG JSON
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- Chuẩn JSON mặc định CHỈ hỗ trợ: dict, list, tuple, str, int, float, bool, None.
- Nếu bạn cố serialize một đối tượng `datetime`, `set`, hoặc một instance của `class` tự tạo, Python sẽ báo lỗi: `TypeError: Object of type ... is not JSON serializable`.
- 👉 **Giải pháp Serialization**: Truyền hàm tùy chỉnh vào tham số `default` của `json.dumps()` (hoặc kế thừa `json.JSONEncoder`).
- 👉 **Giải pháp Deserialization**: Sử dụng tham số `object_hook` của `json.loads()` để tái tạo lại đối tượng ban đầu.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Lưu trữ các Model đối tượng phức tạp trong cơ sở dữ liệu hoặc hệ thống Cache Redis.
- Giao tiếp dữ liệu có trường thời gian ISO 8601 (`datetime.now()`).
=============================================================================
"""

import json
from datetime import datetime, date
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# Định nghĩa một Class người dùng trong ứng dụng
class Member:
    def __init__(self, member_id, full_name, joined_date, roles=None):
        self.member_id = member_id
        self.full_name = full_name
        self.joined_date = joined_date
        self.roles = roles or set()

    def __repr__(self):
        return f"<Member id={self.member_id} name='{self.full_name}' roles={self.roles}>"

def custom_json_serializer(obj):
    """
    Hàm encoder tùy biến xử lý các kiểu dữ liệu không chuẩn JSON:
    - datetime / date -> chuỗi ISO (YYYY-MM-DDTHH:MM:SS)
    - set -> list
    - Member object -> dict với trường cờ '__type__'
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, set):
        return list(obj)
    if isinstance(obj, Member):
        return {
            "__type__": "Member",
            "member_id": obj.member_id,
            "full_name": obj.full_name,
            "joined_date": obj.joined_date.isoformat(),
            "roles": list(obj.roles)
        }
    raise TypeError(f"Đối tượng kiểu {type(obj)} không thể serialize sang JSON!")

def custom_json_decoder(dct):
    """
    Hàm decoder tùy biến tái tạo lại đối tượng Member ban đầu từ JSON dict
    """
    if dct.get("__type__") == "Member":
        return Member(
            member_id=dct["member_id"],
            full_name=dct["full_name"],
            joined_date=datetime.fromisoformat(dct["joined_date"]),
            roles=set(dct["roles"])
        )
    return dct

def main():
    print("=" * 60)
    print("SERIALIZATION ĐỐI TƯỢNG TÙY CHỈNH & DATETIME")
    print("=" * 60)

    # Khởi tạo đối tượng phức tạp
    member = Member(
        member_id=501,
        full_name="Nguyễn Thị Mai",
        joined_date=datetime(2026, 9, 12, 14, 30, 0),
        roles={"Admin", "Editor"}
    )

    print(f"Đối tượng ban đầu trong Python:\n-> {member}\n")

    # 1. Chuyển đối tượng sang JSON
    json_str = json.dumps(
        member,
        default=custom_json_serializer,
        indent=4,
        ensure_ascii=False
    )
    print("Chuỗi JSON sau khi serialize tùy chỉnh:")
    print(json_str)

    # 2. Khôi phục lại đối tượng ban đầu
    print("\n" + "=" * 60)
    print("DESERIALIZATION KHÔI PHỤC ĐỐI TƯỢNG VỚI object_hook")
    print("=" * 60)

    reconstructed_member = json.loads(json_str, object_hook=custom_json_decoder)
    print(f"Đối tượng sau khi khôi phục:\n-> {reconstructed_member}")
    print(f"Kiểu dữ liệu: {type(reconstructed_member)}")
    print(f"Kiểu của joined_date: {type(reconstructed_member.joined_date)}")
    print(f"Kiểu của roles: {type(reconstructed_member.roles)}")

if __name__ == "__main__":
    main()

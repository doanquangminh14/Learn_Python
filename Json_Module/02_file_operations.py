"""
=============================================================================
BÀI 2: ĐỌC VÀ GHI FILE JSON TRỰC TIẾP (json.dump & json.load)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `json.dump(obj, fp)`: (Dump to File) Ghi trực tiếp đối tượng Python vào một file stream (`fp`) mà không cần tạo chuỗi trung gian trong bộ nhớ.
- `json.load(fp)`: (Load from File) Đọc trực tiếp dữ liệu từ file stream (`fp`) và chuyển đổi thành đối tượng Python.
- Luôn mở file với `encoding="utf-8"` để đảm bảo tương thích đa nền tảng và bảo toàn ký tự tiếng Việt.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Lưu trữ kết quả cào dữ liệu (Web Scraping).
- Đọc file danh mục sản phẩm, cấu hình máy chủ.
=============================================================================
"""

import json
import os
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("ĐỌC VÀ GHI FILE JSON (json.dump & json.load)")
    print("=" * 60)

    filename = "products_catalog.json"

    catalog_data = {
        "store_name": "Tech Store Việt Nam",
        "last_updated": "2026-09-12",
        "products": [
            {
                "id": "PROD-01",
                "name": "Bàn phím cơ Không Dây",
                "price": 1250000,
                "in_stock": True,
                "tags": ["phụ kiện", "gaming", "bluetooth"]
            },
            {
                "id": "PROD-02",
                "name": "Màn hình 4K IPS 27 inch",
                "price": 8900000,
                "in_stock": True,
                "tags": ["màn hình", "4k", "đồ họa"]
            },
            {
                "id": "PROD-03",
                "name": "Chuột công thái học Ergonomic",
                "price": 950000,
                "in_stock": False,
                "tags": ["văn phòng", "không dây"]
            }
        ]
    }

    # 1. Ghi dữ liệu vào file bằng json.dump()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(catalog_data, f, indent=4, ensure_ascii=False)
    print(f"1. ✅ Đã ghi dữ liệu thành công vào file: '{filename}'")

    # 2. Đọc lại dữ liệu từ file bằng json.load()
    with open(filename, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)

    print(f"\n2. 📖 Đọc dữ liệu từ file '{filename}':")
    print(f"   - Tên cửa hàng: {loaded_data['store_name']}")
    print(f"   - Tổng số sản phẩm: {len(loaded_data['products'])}")
    print("\n   Danh sách sản phẩm còn hàng:")
    for item in loaded_data["products"]:
        if item["in_stock"]:
            print(f"   * [{item['id']}] {item['name']}: {item['price']:,} VNĐ")

    # 3. Dọn dẹp file demo
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\n3. 🧹 Đã dọn dẹp file thử nghiệm '{filename}'!")

if __name__ == "__main__":
    main()

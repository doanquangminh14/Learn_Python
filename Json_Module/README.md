# 📦 Module `json` Trong Python (JavaScript Object Notation Serialization)

Module `json` cung cấp các công cụ chuẩn giúp chuyển đổi qua lại giữa các kiểu dữ liệu trong Python (Dictionary, List, Tuple, String, Number, Boolean, None) và định dạng văn bản **JSON (JavaScript Object Notation)**.

---

## 🧠 1. Nguyên Lý Hoạt Động Của `json`

- **Tuần tự hóa (Serialization / Encoding)**: Quá trình chuyển đổi cấu trúc dữ liệu trong bộ nhớ RAM của Python thành một chuỗi văn bản JSON (String) hoặc ghi ra file `.json`.
- **Giải tuần tự hóa (Deserialization / Decoding)**: Quá trình đọc một chuỗi JSON hoặc file `.json` và phân tích cú pháp (parse) để dựng lại thành Dictionary hoặc List trong Python.

### 🔄 Bảng Ánh Xạ Kiểu Dữ Liệu Python <-> JSON:

| Kiểu Dữ Liệu Python | Kiểu Dữ Liệu JSON Tương Ứng |
| :--- | :--- |
| `dict` | `object` (cặp `{ "key": value }`) |
| `list`, `tuple` | `array` (`[1, 2, 3]`) |
| `str` | `string` (`"text"`) |
| `int`, `float` | `number` (`42`, `3.14`) |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

---

## 🎯 2. Khi Nào Nên Sử Dụng `json`? (Use Cases Thực Tế)

1. **Giao tiếp REST API & Web Services**: Trao đổi dữ liệu giữa Python Backend (FastAPI, Flask, Django) và Frontend (React, Vue, Mobile App).
2. **Lưu trữ Cấu hình Ứng dụng (Config Files)**: Quản lý cài đặt phần mềm (`config.json`, `settings.json`) một cách trực quan, dễ đọc và chỉnh sửa.
3. **Lưu trữ Dữ liệu Bán Cấu trúc (NoSQL / Document Storage)**: Lưu trữ dữ liệu log, phiên làm việc người dùng, cấu hình game.

---

## 📚 3. Danh Sách Các Bài Thực Hành Trong Thư Mục

| File | Nội Dung Trọng Tâm |
| :--- | :--- |
| [`01_basic_serialization.py`](01_basic_serialization.py) | Làm chủ `dumps()` và `loads()`, các tùy chọn format `indent`, `sort_keys`, `ensure_ascii=False` |
| [`02_file_operations.py`](02_file_operations.py) | Đọc ghi trực tiếp file `.json` bằng `dump()` và `load()`, xử lý chuẩn tiếng Việt UTF-8 |
| [`03_custom_objects.py`](03_custom_objects.py) | Tuần tự hóa kiểu dữ liệu nâng cao (`datetime`, `set`, `Class OOP`) bằng `default` và `object_hook` |
| [`04_safe_config_manager.py`](04_safe_config_manager.py) | Xây dựng hệ thống quản lý file cấu hình `config.json` an toàn, bắt lỗi `JSONDecodeError` |

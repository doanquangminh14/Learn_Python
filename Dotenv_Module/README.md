# 🔐 Module `python-dotenv` Trong Python

Thư viện `python-dotenv` giúp bạn đọc các cặp **key-value** từ file `.env` và tự động nạp chúng vào biến môi trường hệ thống (`os.environ`). Đây là tiêu chuẩn vàng trong phát triển ứng dụng (tuân theo nguyên lý **The Twelve-Factor App**) nhằm bảo mật thông tin nhạy cảm và quản lý cấu hình linh hoạt.

---

## 🧠 1. Tại Sao Cần Dùng `.env` và `python-dotenv`?

1. **Bảo mật bí mật (Secrets Management)**: Tránh hardcode mật khẩu DB, API Key, Secret Token trực tiếp vào mã nguồn.
2. **Không làm rò rỉ mã bí mật lên Git**: File `.env` chứa thông tin nhạy cảm sẽ được thêm vào `.gitignore`, không bao giờ commit lên GitHub/GitLab.
3. **Đa môi trường (Multi-environment)**: Dễ dàng cấu hình các môi trường khác nhau: Development, Staging, Production mà không cần thay đổi source code.
4. **Tách biệt Cấu hình (Config) khỏi Mã nguồn (Code)**: Giúp codebase chuyên nghiệp, dễ bảo trì và mở rộng.

---

## 📦 2. Cài Đặt Thư Viện

```bash
pip install python-dotenv
```

---

## 🎯 3. Nguyên Lý Hoạt Động & Quy Trình Chuẩn

```
📁 Thư mục dự án
├── 📄 .env.example      <-- Đẩy lên Git (Mẫu cấu hình không chứa mật khẩu thực)
├── 📄 .env              <-- Thêm vào .gitignore (Chứa thông tin mật thật)
├── 📄 .gitignore        <-- Khai báo .env
└── 📄 app.py            <-- Dùng load_dotenv() để nạp biến vào os.environ
```

---

## 📚 4. Danh Sách Các Bài Thực Hành Trong Thư Mục

| File | Nội Dung Trọng Tâm |
| :--- | :--- |
| [`.env.example`](.env.example) | File mẫu khai báo các biến môi trường chuẩn cho dự án |
| [`01_load_dotenv_basic.py`](01_load_dotenv_basic.py) | Nạp file `.env` với `load_dotenv()`, đọc biến qua `os.getenv()`, ép kiểu dữ liệu và giá trị mặc định |
| [`02_dotenv_values_dict.py`](02_dotenv_values_dict.py) | Đọc cấu hình trực tiếp vào Dictionary (`dotenv_values`) mà không làm bẩn `os.environ` |
| [`03_variable_expansion_and_override.py`](03_variable_expansion_and_override.py) | Mở rộng biến nội suy (Variable Expansion `${VAR}`), cơ chế ghi đè `override=True/False` |
| [`04_programmatic_env_updates.py`](04_programmatic_env_updates.py) | Thao tác ghi/sửa/xóa key trong file `.env` bằng code với `set_key()` và `unset_key()` |

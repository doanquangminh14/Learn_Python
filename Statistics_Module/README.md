# 📊 Module `statistics` Trong Python (Mathematical Statistics Functions)

Module `statistics` là thư viện chuẩn được tích hợp sẵn từ Python 3.4+, cung cấp các hàm toán học thống kê mô tả (Descriptive Statistics) và suy luận cơ bản với độ chính xác cao mà không cần cài đặt thêm thư viện bên ngoài (như NumPy hay SciPy).

---

## 🧠 1. Nguyên Lý Hoạt Động Của `statistics`

- Hoạt động trực tiếp trên các cấu trúc dữ liệu cơ bản của Python (`list`, `tuple`, `generator`, `iterators`).
- Hỗ trợ các kiểu số thực (`float`), số nguyên (`int`), phân số (`fractions.Fraction`) và số thập phân độ chính xác cao (`decimal.Decimal`).
- Phân biệt rõ ràng giữa **Mẫu (Sample - $n-1$)** và **Tổng thể (Population - $N$)**:
  - Độ lệch chuẩn mẫu: `stdev()` chia cho $n-1$ (hiệu chỉnh Bessel).
  - Độ lệch chuẩn tổng thể: `pstdev()` chia cho $N$.

---

## 🎯 2. Khi Nào Nên Sử Dụng `statistics`? (Use Cases Thực Tế)

1. **Ứng dụng nhẹ không phụ thuộc thư viện ngoài (Zero Dependency)**: Viết script chạy trên môi trường hạn chế hoặc không được cài thư viện C ngoài (`numpy`).
2. **Phân tích Xu hướng & Tỷ lệ Tăng trưởng**:
   - `geometric_mean()`: Tính tỷ lệ tăng trưởng tài chính, lãi suất kép, tỷ suất lợi nhuận đầu tư.
   - `harmonic_mean()`: Tính tốc độ trung bình, tỷ số P/E trung bình trong chứng khoán.
3. **Phân tích Tương quan & Dự báo Tuyến tính**:
   - `correlation()`: Đánh giá mối quan hệ giữa chi phí quảng cáo và doanh thu.
   - `linear_regression()`: Dự đoán doanh thu tháng tới dựa trên xu hướng quá khứ.
4. **Phân chia Phân vị & Boxplot**:
   - `quantiles()`: Phân loại nhóm khách hàng (Top 25% VIP, 50% Phổ thông).

---

## 📚 3. Danh Sách Các Bài Thực Hành Trong Thư Mục

| File | Nội Dung Trọng Tâm |
| :--- | :--- |
| [`01_central_tendency.py`](01_central_tendency.py) | Xu hướng tập trung: `mean`, `fmean`, `median`, `mode`, `multimode`, `geometric_mean`, `harmonic_mean` |
| [`02_dispersion_and_spread.py`](02_dispersion_and_spread.py) | Độ phân tán: Phương sai `variance`, độ lệch chuẩn `stdev` vs `pstdev`, tứ phân vị `quantiles` |
| [`03_correlation_and_regression.py`](03_correlation_and_regression.py) | Hệ số tương quan Pearson `correlation()` và Hồi quy tuyến tính đơn biến `linear_regression()` |
| [`04_sales_and_grades_analysis.py`](04_sales_and_grades_analysis.py) | Case Study thực tế: Phân tích kết quả học tập và báo cáo hiệu suất kinh doanh |

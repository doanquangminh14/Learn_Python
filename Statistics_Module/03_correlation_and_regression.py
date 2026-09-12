"""
=============================================================================
BÀI 3: HỆ SỐ TƯƠNG QUAN VÀ HỒI QUY TUYẾN TÍNH (Correlation & Linear Regression)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `statistics.correlation(x, y)`: Tính hệ số tương quan Pearson $r$ giữa hai tập dữ liệu:
  - $r = 1$: Tương quan thuận hoàn hảo (x tăng thì y tăng tuyệt đối).
  - $r = -1$: Tương quan nghịch hoàn hảo (x tăng thì y giảm tuyệt đối).
  - $r \approx 0$: Không có mối tương quan tuyến tính.
- `statistics.linear_regression(x, y)`: Xây dựng mô hình hồi quy tuyến tính đơn biến $y = \text{slope} \cdot x + \text{intercept}$.
  - Trả về đối tượng `LinearRegression(slope=..., intercept=...)`.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Đo lường mức độ ảnh hưởng của ngân sách Marketing lên Doanh số bán hàng.
- Dự đoán giá nhà dựa trên diện tích mét vuông.
=============================================================================
"""

import statistics
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. TÍNH HỆ SỐ TƯƠNG QUAN PEARSON (statistics.correlation)")
    print("=" * 60)

    # Dữ liệu: Số giờ ôn thi (x) và Điểm số đạt được (y) của 7 sinh viên
    study_hours = [1, 2, 3, 4, 5, 6, 7]
    exam_grades = [4.5, 5.0, 6.2, 7.0, 8.1, 8.8, 9.5]

    r = statistics.correlation(study_hours, exam_grades)
    print(f"Số giờ ôn tập: {study_hours}")
    print(f"Điểm số:       {exam_grades}")
    print(f"\n-> Hệ số tương quan r = {r:.4f}")

    if r > 0.8:
        print("-> Đánh giá: Có mối tương quan thuận RẤT MẠNH (học càng nhiều giờ điểm càng cao).")
    elif r > 0.5:
        print("-> Đánh giá: Tương quan thuận mức độ vừa phải.")
    else:
        print("-> Đánh giá: Tương quan yếu.")

    print("\n" + "=" * 60)
    print("2. HỒI QUY TUYẾN TÍNH & DỰ BÁO TƯƠNG LAI (statistics.linear_regression)")
    print("=" * 60)

    # Xây dựng mô hình đường thẳng dự đoán y = a*x + b
    model = statistics.linear_regression(study_hours, exam_grades)
    slope = model.slope          # Hệ số góc (a)
    intercept = model.intercept  # Hệ số tự do (b)

    print(f"Phương trình hồi quy tuyến tính:")
    print(f"  Điểm_Số = ({slope:.3f} * Số_Giờ_Học) + {intercept:.3f}")

    # Dự đoán điểm số cho sinh viên học 8.5 giờ và 10 giờ
    test_hours = [8.5, 10.0]
    print("\n🔮 Dự báo điểm số:")
    for h in test_hours:
        predicted_grade = min(10.0, slope * h + intercept) # Giới hạn tối đa 10 điểm
        print(f"  * Nếu học {h} giờ -> Dự kiến đạt: {predicted_grade:.2f} điểm")

if __name__ == "__main__":
    main()

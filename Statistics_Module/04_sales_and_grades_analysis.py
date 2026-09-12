"""
=============================================================================
BÀI 4: PHÂN TÍCH HIỆU SUẤT KINH DOANH VÀ KẾT QUẢ HỌC TẬP THỰC TẾ
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- Kết hợp tổng hợp các hàm trong module `statistics`: `fmean`, `median`, `stdev`, `quantiles`, `linear_regression`.
- Tự động hóa báo cáo phân tích số liệu thống kê (Data Analytics Report) cho doanh nghiệp.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Xây dựng dashboard báo cáo tài chính hàng tháng.
- Đánh giá chất lượng lớp học và phát hiện sinh viên cần hỗ trợ học tập.
=============================================================================
"""

import statistics
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def generate_business_report():
    """Phân tích doanh thu 12 tháng của chuỗi cửa hàng (đơn vị: triệu VNĐ)"""
    print("=" * 60)
    print("BÁO CÁO PHÂN TÍCH DOANH THU NĂM (STATISTICS REPORT)")
    print("=" * 60)

    monthly_sales = [
        120, 135, 128, 142, 160, 175,
        180, 195, 210, 205, 230, 290 # Tháng 12 mua sắm Tết tăng cao
    ]
    months = list(range(1, 13))

    total = sum(monthly_sales)
    avg_sales = statistics.fmean(monthly_sales)
    med_sales = statistics.median(monthly_sales)
    std_sales = statistics.stdev(monthly_sales)
    q1, q2, q3 = statistics.quantiles(monthly_sales, n=4)

    # Dự báo xu hướng tuyến tính cho 3 tháng đầu năm tiếp theo (tháng 13, 14, 15)
    trend_model = statistics.linear_regression(months, monthly_sales)

    print(f"1. 📊 Tổng Quan Doanh Số:")
    print(f"   - Tổng doanh thu cả năm:     {total:,} triệu VNĐ")
    print(f"   - Doanh thu trung bình/tháng: {avg_sales:.2f} triệu VNĐ")
    print(f"   - Trung vị doanh thu:         {med_sales:.2f} triệu VNĐ")
    print(f"   - Độ biến động (stdev):       ±{std_sales:.2f} triệu VNĐ")
    
    print(f"\n2. 📈 Phân Vị Hiệu Suất Bán Hàng:")
    print(f"   - Ngưỡng tháng kém (Q1 - 25%):   < {q1:.1f} triệu VNĐ")
    print(f"   - Ngưỡng tháng khá (Q3 - 75%):   >= {q3:.1f} triệu VNĐ")
    print(f"   - Khoảng chênh lệch (IQR):       {q3 - q1:.1f} triệu VNĐ")

    print(f"\n3. 🔮 Dự Báo Doanh Thu Năm Mới (Tăng trưởng bình quân +{trend_model.slope:.1f} tr/tháng):")
    for next_month in [13, 14, 15]:
        forecast = trend_model.slope * next_month + trend_model.intercept
        print(f"   * Tháng {next_month - 12} năm tới: Dự kiến ~ {forecast:.1f} triệu VNĐ")

if __name__ == "__main__":
    generate_business_report()

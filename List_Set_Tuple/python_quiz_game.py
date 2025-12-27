questions = ("Bạn tên thật là gì?",
             "Bạn bao nhiêu tuổi?",
             "Cung của bạn là gì?",
             "Bạn đang học ngành gì?",
             "Môn thể thao bạn yêu thích?")
options = (("A.Nguyễn Thị Hồng","B.Trần Thu Phương","C.Đoàn Thị Sáu","D.Đoàn Quang Minh"),
           ("A.12","B.20","C.21","D.29"),
           ("A.Thiên Bình","B.Bọ Cạp","C.Xử Nữ","D.Bảo Bình"),
           ("A.Kế toán","B.Công Nghệ Thông Tin","C.Maketing","D.Y"),
           ("A.Cầu lông","B.Đá cầu ","C.Nhảy","D.Đá bóng"))

answers = ("D","B","A","B","C")
guess = []
score = 0
question_num = 0


for question in questions:
    print("------------------------------")
    print(question)
    for answer in options[question_num]:
        print(answer)
    z = input("Đáp án(A,B,C,D): ").upper()
    if z == answers[question_num]:
        print("Đáp án đúng")
        score += 1
    else:
        print(f"Đáp án sai. Đáp án đúng là: {answers[question_num]}")
    guess.append(z)
    question_num += 1
print("------------------------------")
print("Đáp án bạn chọn là: ")
for x in guess: 
    print(x,end= " ")
print()
print("Đáp án đúng là :")
for x in answers:
    print(x, end = " ")
print()
score = score/len(questions) * 100
print(f"Điểm bạn đạt được là: {score}")
# Cocession stand program
menu = {"garan": 20000,"banhbao": 15000,"mitron": 35000,"nuocsuoi" : 6000}
cart = []
total = 0
print("-----------------Menu----------------------")
for key,value in menu.items():
    print(f"{key:10}: {value:.2f}")
while True:
    food = input("Món bạn chọn là(q để thoát): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None: 
        cart.append(food)
print("---------------------------------------")
for food in cart:
    total += menu.get(food)
    print(food,end = " ")
print()
print(f"Giá phải trả: {total} VNĐ")
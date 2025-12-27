# Shopping cart program
foods = []
prices = []
total = 0

while True:
    food = input("Nhập món ăn bạn muốn mua(q để thoát):")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Giá của {food} mà bạn phải trả là : VND "))
        prices.append(price)
print("----Hóa đơn của bạn----")
for x in foods:
    print(x, end = " ")
print()
for y in prices:
    total += y

print(f"Tổng : {total:.3f}")

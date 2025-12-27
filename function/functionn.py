##1.positional
# def cong(x,y):
#     z = x+y
#     return z
# print(cong(3,4))

##2.default
# def cong(x,y=0,z=0.05):
#     return x*(1-y)*(1+z)
# print(cong(500))
# print(cong(500,0.1))
# print(cong(500,0.1,0))

import time

# def count(start,end):
#     for x in range (start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
# count(0,10)

# def count(end,start=0):
#     for x in range (start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
# count(10)
# count(30,15)


##3.Keyword
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello",title="Mr.",first="Minh",last="Doan")

# def get_phone(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(1,123,456,7890)
# phone_num1 = get_phone(country=1,area=123,first=456,last=7890)
# print(phone_num)
# print(phone_num1)

##4.Arbitrary
# *args  = allow you to pass mutiple non-key arguments
# *kwargs= allow you to pass mutiple keywork-arguments
#          * unpacking operator

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4,5))

# def bcc(*args):
#     for arg in args:
#         print(arg, end = " ")
# bcc("a","B","C")   

# def print_address(**kwargs):
#     print(kwargs.keys())
#     for key in kwargs.keys():
#         print(key,end = " ")
#     print()
#     print(kwargs.values())
#     for value in kwargs.values():
#         print(value,end = " ")
#     print()
#     for key,value in kwargs.items():
#         print(f"{key:10}: {value}")
# print_address(street= "123 Fake St." , city= "Detroit", state="MI", zip= "54321")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end= " ")
    print()
    for value in kwargs.values():
        print(value, end = " ")
    print()

    if "apt" in kwargs:
      print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
       print(f"{kwargs.get('street')} ") 
       print(f"{kwargs.get('pobox')} ")
    else:
        print(f"{kwargs.get('street')} ")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants","III",
               street="123 Fake St.",
               city="Detroit",
               #apt="#100",
               pobox= "P0 box #1001",
               state="MI",
               zip= "54321")
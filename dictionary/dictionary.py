# dictionary = a collection of {key:value} pairs
#              odered and changeagle. No duplicates

bcc = {"A": "10", "B": "12","C": "19","D": "11"}
#print(dir(bcc))
#print(help(bcc))
print(bcc.get("A"))

#if bcc.get("A"):
#    print("Co")
#else:
#    print("Khong")

#bcc.update({"E": "45"})
#bcc.pop("A")
#bcc.popitem()
#bcc.clear()

#keys = bcc.keys()
#for key in bcc.keys():
#    print(key)

# values = bcc.values()
for value in bcc.values():
    print(value)

# items = bcc.items()
# for key, value in bcc.items():
#     print(f"{key}: {value}")
# print(items)
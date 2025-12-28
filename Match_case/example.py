# def thu(day):
#     match day:
#         case 1:
#             return "Hom nay CN"
#         case 2:
#             return "Hom nay thu hai"
#         case _:
#             return "Khong co thu nay OK!"
# print(thu("ko"))

# def thu(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False
#         case _:
#             return False
# print(thu("MI"))       

def thu(day):
    match day:
        case "Sunday" | "Tuseday":
            return True
        case "Monday" | "Wednesday":
            return False
        case _:
            return False
print(thu("Tuseday"))    
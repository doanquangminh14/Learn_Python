# collection = single "variable" used to store multiple value
# List = [] ordered and changeable. Duplicate OK
#bcc = ["a","c","b","e","d","f","a"]
#print(bcc[0:6:2])
#for x in bcc:
 #   print(x,end = " ")
#print(dir(bcc))
#print(help(bcc))
#print(len(bcc))
#print("d" in bcc)
#bcc[5] = "g"

#for x in bcc: 
   # print(x, end = " ")
#bcc.append("g")
#bcc.remove("a")
#bcc.insert(5,"g")
#bcc.sort()
#bcc.reverse()
#bcc.clear()
#print(bcc.index("f"))
# print(bcc.count("a"))
# print(bcc)

#---------------------------------------------------------------------------------------
# List comprehension = A consise to creat lists in python 
#                      Conpact and easier to read than tradittional loops 
#                      [experssion for value in iterable if condition]
#---------------------------------------------------------------------------------------

# double = []
# for x in range(1,11):
#     double.append(x*2)
# print(double)

# doubles = [x*2 for x in range(1,11)]
# triples = [y*3 for y in range(1,11)]
# squares = [z*z for z in range(1,11)]
# print(squares)

# bccs = ["apple","bread","cat","dog"]
# bccs = [bcc.upper() for bcc in bccs ]
# bcc_char = [bcc[0] for bcc in bccs ]
# print(bccs)

# numbers = [1,-2,-4,5,7,8]
# positive_nums = [num for num in numbers if num >=0]
# negative_nums = [num for num in numbers if num <0]
# even_num = [num for num in numbers if num % 2 ==0]
# old_num = [num for num in numbers if num % 2 ==1]
# print(old_num)

grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
"""
x = ["1","2","3","4","5"]
y= ["6","7","8","9"]
z=["10","11","12"]

tong = [x,y,z]
print(tong)
print(tong[1])
print(tong[0][2])

"""

"""
tong = [["1","2","3","4","5"],["6","7","8","9"],["10","11","12"]]  # set , tuple cũng được
for x in tong:
     for y in x:
          print(y,end = " ")
     print()
"""


num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for x in num_pad:
    for num in x:
        print(num,end = " ")
    print()

     
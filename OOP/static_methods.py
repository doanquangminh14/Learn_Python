# Static methods = A methods that belong to a class rather than any object from that class(instance)
#                  Usually used for general utility functions

# Intance methods = Best for operations on instances of the class (object)
#Static methods = Best for utility functions that  do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name 
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod # Không cần phải khai báo intances
    def is_valib_position(position):
        valib_position = ["Manager","Cashier","Cook","janitor"]
        return position in valib_position
    
employee1 = Employee("Euguen","Manager")
employee2 = Employee("Squidward","Cashier")
employee3 = Employee("Spongebob","Cook")

print(Employee.is_valib_position("Rocket Scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
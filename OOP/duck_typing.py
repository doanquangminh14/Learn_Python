# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                Object must have the minimum necessary attributes/methods
#                "If it look like a duck and quacks like a duck, it must be a duck."

class Animals:
    alive = True

class Dog(Animals):
    def speak(self):
        print("Gau!")

class Cat(Animals):
    def speak(self):
        print("MEW!")

class Car:
    alive = True
    def speak(self):
        print("HONK!")

animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
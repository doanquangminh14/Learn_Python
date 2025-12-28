# multiple inheritance = inherit from more than one parent class
#                        C(A,B)
# multiple inheritance = inherit from a parent which inherrits from another parent
#                        C(B) <- B(A) <- A
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
       print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("nemo")

fish.hunt()
rabbit.eat()
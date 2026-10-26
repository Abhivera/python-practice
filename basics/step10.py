class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof"
    
    def birthday(self):
        self.age +=1

d = Dog("Pluto", 5)
print(d.bark())
d.birthday()

print(d.age)

class Puppy(Dog):
    def bark(self):
        return f"{self.name} says yip"

print(Puppy("Moti",1).bark())      
class Animal:
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return self.sound
    
    def __str__(self):
        return self.sound
class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Cow(Animal):
    pass

my_cat = Cat("Meow")
print(my_cat)
my_dog = Dog("Woof")
print(my_dog)
my_cow= Cow("Moo")
print(my_cow)
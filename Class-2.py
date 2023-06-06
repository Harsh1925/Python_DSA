class Animal:

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("Woof!!")


New_Dog = Dog()
New_Dog.who_am_i()
New_Dog.eat()
New_Dog.bark()

# This is new

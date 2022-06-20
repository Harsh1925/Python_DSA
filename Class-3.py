class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " Wooff!!!"


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " Meow!!!"


rocky = Dog("rocky")
print(rocky.speak())
niko = Cat("niko")
print(niko.speak())
print()

for pet in [rocky, niko]:
    print(type(pet))
    print(pet.speak())
    print()


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(rocky)

class Dog():

    species = 'mammal'

    def __init__(self, mybreed, name, spots):
        self.breed = mybreed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print("Woooff My name is {} and the number is {}".format(self.name, number))


my_dog = Dog('Huskie', 'Sammy', False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark(2)

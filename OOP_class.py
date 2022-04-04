def say_hello(name='Ramesh'):
    print("Hello " + name)


say_hello("Harsh")


def even_num(num_list):
    num = []

    for i in num_list:
        if i % 2 == 0:
            num.append(i)
        else:
            pass

    return num


var = even_num([1, 2, 3, 4, 5, 6, 7, 8])
print(var)

#----------------------------------------------------

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]


def emp_check(work_hour):
    cur_max = 0
    emp_of_month = ''

    for i, j in work_hour:
        if j > cur_max:
            cur_max = j
            emp_of_month = i

    print(emp_of_month)


emp_check(work_hours)

#----------------------------------------------------------


class Pet:
    number_of_pets = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.number_of_pets += 1

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    @staticmethod
    def speak():
        print("I don't know what to say")


class Cat(Pet):

    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and i am {self.age} year old and I am {self.colour} colour")


class Dog(Pet):

    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Bill", 19)
p.show()
p.speak()
print("-----------------")
d = Dog("Tim", 21)
d.speak()
print("-----------------")
c = Cat("Ramesh", 23, "brown")
c.show()
c.speak()
print("-----------------")
f = Fish("machli", 4)
f.speak()
print("===================")
print(f"Number of pets are {Pet.number_of_pets}")

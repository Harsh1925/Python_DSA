name = 'harsh'

if name == 'harsh':
    print('Hello harsh')
else:
    print('Hello Ramesh')

# ------------------------------------------------------

from random import randint

print((randint(0, 200)))

""""""
result = input('Enter your name: ')

print(result)

""""""


def say_hello(name='Ramesh'):
    print("Hello " + name)


say_hello("Harsh")


def addition(num1, num2):
    return num1 + num2


result = addition(10, 20)
print(result)


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

""""""

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



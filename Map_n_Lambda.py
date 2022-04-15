def square(num):
    num = num ** 2
    return num


my_list = [1, 2, 3, 4, 5]

"""

for item in map(square, my_list):
    print(item)
"""

print(list(map(square, my_list)))


# ---------------------------------------

def slicer(name):
    if len(name) % 2 == 0:
        return 'Even'
    else:
        return name[0]


my_names = ['Andy', 'Eve', 'Sally']
print(list(map(slicer, my_names)))


# -----------------------------------------

def check_even(num):
    return num % 2 == 0


my_num = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, my_num)))  # in filter only include boolean type function

"""
for item in filter(check_even, my_num):
    print(item)
"""


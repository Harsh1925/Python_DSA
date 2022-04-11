my_list = [1, 2, 3, 4, 5, 6]

for i in my_list:
    print(i)
    print('hello')

for i in my_list:
    if i % 2 == 0:
        print(f'Even number: {i}')
    else:
        print(f'Odd number : {i}')

list_num = 0
for j in my_list:
    list_num = list_num + j

print(list_num)

#------------------------

my_string = 'Hello World'
for letter in my_string:
    print(letter)

for letter in ' newworld':
    print(letter)

my_string = 'Hello World'
for letter in my_string:
    print("Coooooool!!!")

#--------------------------

tup = (1, 2, 3)
for i in tup:
    print(i)

new_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(new_list))

for item in new_list:
    print(item)

for a, b in new_list:
    print(a)
    print(b)

#----------------------------

mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in mylist:
    print(b)

#------------------------------

d = {'k1': 10, 'k2': 2, 'k3': 3}

for item in d.items():
    print(item)

d = {'k1': 10, 'k2': 2, 'k3': 3}

for item in d.values():
    print(item)

for key, item in d.items():
    print(key)
    print(item)

#---------------------------------

word = 'abcde'

for index, item in enumerate(word):
    print(index)
    print(item)

mylist = [1,2,3]
mylist2 = ['a', 'b', 'c']

for item in zip(mylist, mylist2):
    print(item)

print(list(zip(mylist, mylist2)))

x = [(1,2,3),(4,5,6),(7,8,9)]

print('x' in ['x','y','z'])

# -------------------------------------------------------

Mylist = ['a', 'b', 'c']
print(''.join(Mylist))

mystring = 'hellow'
mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

mylist2 = [letter for letter in mylist]  # for ni aagar and paachhar varo variable same hovo joi ae

print(mylist2)

#ok now i am chaning here 
#------------------------------------------------------

mylist = [num ** 2 for num in range(0, 10)]

print(mylist)

#------------------------------------------------------

mylist2 = [x for x in range(0, 11) if x % 2 == 0]

print(mylist2)

#------------------------------------------------------

mylist3 = [x ** 2 for x in range(0, 11) if x % 2 == 0]

print(mylist3)

#------------------------------------------------------

celcius = [0, 10, 21, 34.5]

fahrenheit = [int((9 / 5) * temp + 32) for temp in celcius]

print(fahrenheit)

#------------------------------------------------------

st = 'Sam Print only the words that start with s in this sentence'

for a in st.split():
    if a[0].lower() == 's':
        print(a)

#------------------------------------------------------

for i in range(0, 11):
    if i % 2 == 0:
        print(i)


list_num = [i for i in range(1, 50) if i % 3 == 0]

print(list_num)

#------------------------------------------------------

st = 'Print every word in this sentence that has an even number of letter'

for i in st.split():
    count = 0
    for j in i:
        count = count + 1

    if count % 2 == 0:
        print(f'{i} is Even')

print("")

#------------------------------------------------------

st = 'Print every word in this sentence that has an even number of letter'

for word in st.split():
    if len(word) % 2 == 0:
        print(word + ' is even')

# ------------------------------------------------------

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBizz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Bizz')
    else:
        print(i)

# ------------------------------------------------------

st = 'Create a list of the first letter of every word in this string'
new_list = []
for j in st.split():
    new_list.append(j[0])

print(new_list)

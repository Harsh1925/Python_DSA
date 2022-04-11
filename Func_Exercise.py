# Build function that return lesser number if both numbers are even and return greater number if one or both are odd


def Check_Even(x, y):
    if x % 2 == 0 and y % 2 == 0:

        if x > y:
            return y
        else:
            return x

    elif x == y:
        return 0

    else:

        if x > y:
            return x
        else:
            return y


"""

    if x % 2 == 0 and y % 2 == 0:
        return min(x, y)
    
    else:
        return max(x, y)
        
"""

value = Check_Even(2, 4)

if value == 0:
    print("Both values are same")
else:
    print(value)


# ----------------------------------------------------------------------

# write function that take two string and return true if both string start with same latter and return false if not


def check_string():
    print("Enter two string with space in between")
    arr = input()
    str_value = arr.lower().split()

    if str_value[0][0] == str_value[1][0]:
        return True

    else:
        return False


bool_val = check_string()
print(bool_val)


# -----------------------------------------------------------


# write the function that capitalize first and fourth letter of the word


def cap_word(name):
    name = name[0].capitalize() + name[1:3] + name[3].capitalize() + name[4:len(name)]  # name[4:] and name[0].upper()

    return name


"""

 name = name[:3].capitalize() + name[3:].capitalize()
 
 return name

"""

new_word = cap_word('macdonalds')
print("macdonalds")
print(new_word)

# -----------------------------------------------------------------------------------------------

# Write the function that count the number of pattern appear in the string including overlap

"""

def check_pattern(check,word):

    chunk_size = len(check)
    ok = [word[i:i+chunk_size] for i in range(0, len(word),chunk_size)]
    number = len(ok)
    print(ok)
    count = 0

    for new in range(0,len(ok)):

        if ok[new] == check:

            count = count + 1

    return count


num = check_pattern('hey', 'heyhehey')
print(num)

"""
# --------------------------
"""

def check_pattern(x,y):

    num = y.count(x)

    return num


print(check_pattern('hah','hahahah'))

"""


# ----------------------------


def check_pattern(check, word):
    count = 0
    for i in range(0, len(word)):

        if check[0] == word[i]:

            j = 0
            for j in range(0, len(check)):

                if i + j >= len(word):
                    break

                elif check[j] == word[i + j] and i < len(word) - 1:
                    count = count + 1

    count = count
    count = count / len(check)
    return count


print(check_pattern('hah', 'hahahah'))


# --------------------------------------------------------------------------------

# Write function that return sum except ignore the number after 6 until number 9 comes

def sum_num(number):
    sum_of_num = 0
    bool_value = True
    prev_value = 0

    for i in range(0, len(number)):

        if number[i] == 6:
            bool_value = False

        if bool_value:
            sum_of_num = number[i] + prev_value
            prev_value = sum_of_num

        if number[i] == 9:
            bool_value = True

    return sum_of_num


print(sum_num([4, 5, 6, 7, 8, 9]))
print(sum_num([2, 1, 6, 9, 11]))


# ------------------------------------------------------------------------------------

# Write a function that take list of integer and return true if it contains 007 in order


def check_list(arr):
    count = 0
    for i in range(0, len(arr)):

        if arr[i] == 0:
            count = count + 1

        if arr[i] == 7 and count == 2:
            return True

    return False


print(check_list([1, 7, 2, 0, 4, 5, 0]))
print(check_list([1, 2, 4, 0, 0, 7, 5]))
print(check_list([1, 0, 2, 4, 0, 5, 7]))


# ------------------------------------------------------------------------------------

# write the function that reverse the words of sentence


def rev(text):
    word = text.split()

    return ' '.join(word[::-1])


print(rev("I Love Python"))


# --------------------------------------------------------------------------------------

# Write the function that check prime numbers

def prime(num):
    x = 3

    prime_num = [2]

    while x <= num:

        for y in range(3, x, 2):    # for y in prime_num:

            if x % y == 0:
                x += 2
                break

        else:

            prime_num.append(x)
            x += 2

    return prime_num


print(prime(29))

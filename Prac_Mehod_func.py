# write the function to compute the volume of the sphere given its redius
import string


def vol(rad):
    print((rad ** 3) * 3.14 * (4 / 3))
    print()


vol(2)


# write the function to check whether given number is in range or not

def ran_check(num, low, high):
    print(num in range(low, high + 1))
    print()


ran_check(5, 2, 7)

# -------------------------------------

"""
def ran_check(num, low, high):
    if num < low or num > high:
        print(f"{num} is not in the range between {low} and {high}")
    else:
        print(f"{num} is in the range between {low} and {high} ")

    print()


ran_check(11, 2, 7)
"""


# ----------------------------------------------

# Write the function that accept the string and count the upper and lower case letters

def up_lows(s):
    count_up = 0
    count_low = 0

    for i in s:
        if i.isupper():  # isupper checks is string or letter is in uppercase or not and returns boolean value
            count_up = count_up + 1

        elif i.islower():
            count_low = count_low + 1

    print(f"origin string : {s}")
    print(f"No of upper case letter : {count_up}")
    print(f"No of upper case letter : {count_low}")


s = "Hello Mr. Rogers, how are you this fine Tuesday?"
up_lows(s)
print()


# write the function that take the list and return the list with only unique numbers or elements

def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 2, 2, 2, 3, 3, 4, 5]))
print()


# Write the function to multiply all the number of given list

def multiply(numbers):
    num = 1
    for i in numbers:
        num = i * num
    return num


print(multiply([1, 2, 3, -4]))
print()


# Write the function that check whether given string is palindrome or not

def palindrome(s):
    return s == s[::-1]


print(palindrome("wow"))
print(palindrome('nurses run'))
print()


# write function that check whether given string is palindrome or not , remove spaces between characters

def palindrome1(s1):
    s1 = s1.replace(" ", "")
    return s1 == s1[::-1]


print("sec pali")
print(palindrome1("nurses run"))
print()


# Write the function to check whether given string is pangram or not. # pangram means contain every word from alphabet

def ispangram(str1, alphabet=string.ascii_lowercase):
    length = len(str1)
    for i in alphabet:
        for j in range(length):
            if i == str1[j]:
                break

            elif j == length - 1 and i != str1[j]:
                print(False)
                return 0

    print(True)


ispangram("The quick brown fox jumps over the lazy dog")

print(string.ascii_lowercase)
print()


#-------------------------------------------------------------------

def ispangram1(str1, alphabet=string.ascii_lowercase):

    alphaset = set(alphabet)
    str1 = str1.replace(" ", "")
    str1 = str1.lower()
    str1 = set(str1)
    return  str1 == alphaset


print(ispangram1("The quick brown fox jumps over the lazy dog"))

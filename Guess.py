from random import shuffle


def shuffle_num(my_list):
    shuffle(my_list)
    return my_list


def guess():
    num = input("Enter the number 0, 1, 2 ---> ")
    return num


def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print('Correct')
    else:
        print('Wrong')
        print(my_list)


my_list = ['', 'O', '']
new_list = shuffle_num(my_list)
guess1 = int(guess())
check_guess(new_list, guess1)

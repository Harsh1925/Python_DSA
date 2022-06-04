def myfunc(a, b, c, e=0, f=0):
    print(sum((a, b, c, e, f)) * 0.05)
    return 0


def myfunc2(*args):
    print()
    print(args)
    print(sum(args) * 0.05)
    print()


def myfunc3(*args):
    for item in args:
        print(item)


myfunc(20, 30, 50)
myfunc2(20, 30, 50, 100, 100)
myfunc3(20, 30, 60, 200, 10)
print()


# ----------------------------------------------------
# kwargs => KEY WORD ARGUMENTS


def new_func(**kwargs):
    print(kwargs)

    if 'fruit' in kwargs:
        print("My choice of fruits is here {}".format(kwargs['fruit']))

    else:
        print("I didn't get my fruit but it is {}".format(kwargs['veggie']))


new_func(fruit='Apple')
print()
new_func(veggie='carrot')
print()
new_func(fruit='banana', veggie='tomato')
print()


# ------------------------------------------------------------------


def combined_func(*args, **kwargs):
    print(args, kwargs)

    print("I like to have {} {}".format(args[1], kwargs['product']))


combined_func(10, 20, 30, fruit='apple', product='eggs', animal='Dog')

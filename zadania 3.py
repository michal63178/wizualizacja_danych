from random import randint

# 1
x = {1 - x for x in range(1, 11)}
y = {4 ** x for x in range(8)}
z = {x for x in y if not x & 1}

# 2
li_1 = [randint(0, 9) for x in range(10)]
even = [x for x in li_1 if not x & 1]

# 3
shopping_1 = {k: v for k, v in (('ziemniaki', '1 kg'), ('ogórki', 2),
                                ('pomidory', 5), ('mleko', 1))}
number_of_items = [x[0] for x in shopping_1.items() if type(x[1]) == int]


# 4


def pythagoras(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


# 5


def trapeze(a=0, b=0, h=0):
    return ((a + b) * h) / 2


# 6


def product_1(a=1, b=4, n=10):
    for i in range(n):
        a *= b

    return a


# 7


def product_2(*args):
    product = args[0]

    for i in range(args[2]):
        product *= args[1]

    return product


# 8


def shopping_2(**kwargs):
    return len(kwargs), sum(kwargs.values())

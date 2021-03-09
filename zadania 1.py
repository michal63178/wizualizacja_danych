import math

# 1
a, b = 1, 2
c, d = .3, .4
e, f = 'a', 'b'
g, h = (1, 2), (3, .4)
i, j = [e, f], [a, c]
k, L = {1: 'a'}, {2: 'c'}
m, n = {4, 5, 6}, {9, 8, 7}

print(a, b, c, d, e, f, g, h, i, j, k, L, m, n)


# 2


def correct(number):
    if not number:
        return False

    if number.count('-') > 1:
        return False

    if number.count('.') > 1:
        return False

    idx = number.find('-') - 1

    if idx != -1 and idx != -2:
        return False

    number = set(number)

    for char in number:
        if char not in '.-0123456789':
            return False

    return True


a = input('Podaj liczbę\n')
sign = input('Wpisz odpowiedni znak, aby wybrać działanie\n'
             'dodawanie: +\n'
             'odejmowanie: -\n'
             'mnożenie: *\n'
             'dzielenie: /\n'
             'potęgowanie: ^\n'
             'pierwiastkowanie: prw\n'
             'dzielenie całkowite: //\n'
             'reszta z dzielenia: mod\n')

if sign == 'prw':
    if correct(a):
        a = float(a)

        if a >= 0:
            print(math.sqrt(a))

        else:
            print('Brak rozwiązań w zbiorze liczb rzeczywistych')

    else:
        print('Złe dane')

else:
    b = input('Podaj liczbę\n')

    if (correct(a) and correct(b) and sign in
            ('+', '-', '*', '/', '^', '//', 'mod')):
        a = float(a)
        b = float(b)

        if sign == '+':
            print(a + b)

        elif sign == '-':
            print(a - b)

        elif sign == '*':
            print(a * b)

        elif sign == '^':
            print(a ** b)

        elif b:
            if sign == '/':
                print(a / b)

            elif sign == '//':
                print(a // b)

            elif sign == 'mod':
                print(a % b)

        else:
            print('Nieokreślone')

    else:
        print('Złe dane')

# 3
a = 4
a += 2
a -= 2
a *= 2
a /= 2
a **= 2
a %= 2

# 4
print(math.exp(10))
print((math.log(5 + math.sin(8) ** 2)) ** (1 / 6))
print(int(3.55))
print(int(4.8 + 1))

# 5
name = 'MARIUSZ'
last_name = 'NOWAK'

print(name.capitalize(), last_name.capitalize())

# 6
lyrics = 'Jest wesoło la la la bawimy się la la la'

print(lyrics.count('la'))

# 7
text = 'To jest przykładowy ciąg znaków'

print(text[1], text[-1])

# 8

print(lyrics.split())

# 9
s = 'dsadasfasd'
f = 4.18
h = 0xff

print(f'{s} {f} {h:x}')

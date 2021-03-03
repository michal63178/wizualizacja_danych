import math

# 1
a, b = 1, 2
c, d = .3, .4
e, f = 'a', 'b'
g, h = (1, 2), (3, .4)
i, j = [e, f], [a, c]
k, L = {1: 'a'}, {2: 'c'}
m, n = {4, 5, 6}, {9, 8, 7}

print(a, b, c, d, e, f, g,
      h, i, j, k, L, m, n)

# 2
a = float(input())
b = float(input())
c = input()

if c == '+':
    print(a + b)

elif c == '-':
    print(a - b)

elif c == '*':
    print(a * b)

elif c == '/':
    print(a / b)

elif c == '//':
    print(a // b)

elif c == '^':
    print(a ** b)

elif c == 'prw':
    print(math.sqrt(a))

elif c == 'mod':
    print(a % b)

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
lyrics = 'Jest wesoło la la la wszyscy się bawimy la la la'

print(lyrics.count('la'))

# 7
text = 'To jest przykładowy ciąg znaków.'

print(text[1], text[-1])

# 8

print(lyrics.split())

# 9
s = 'dsadasfasd'
f = 4.18
h = 0xff

print(f'{s} {f} {h:x}')

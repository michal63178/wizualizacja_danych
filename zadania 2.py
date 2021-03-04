from sys import stdin
from sys import stdout
import math

# 1
sports = ['siatkówka', 'ping-pong', 'piłka nożna']
sports.reverse()
sports.extend(['koszykówka', 'piłka ręczna'])

# 2
shortcuts = {
    'al.': 'aleja',
    'cd.': 'ciąg dalszy',
    'cdn.': 'ciąg dalszy nastąpi',
    'CV': 'curriculum vitae',
    'dr': 'doktor',
    'itd.': 'i tak dalej',
    'itp.': 'i tym podobne',
    'lek.': 'lekarz',
    'lic.': 'licencjat',
    'mgr': 'magister',
    'NIP': 'Numer Identyfikacji Podatkowej',
    'np.': 'na przykład',
    'nr': 'numer',
    'PESEL': 'Powszechny Elektroniczny System Ewidencji Ludności',
    'pl.': 'plac',
    'płd.': 'południe, południowy',
    'płn.': 'północ, północny',
    'p.o.': 'pełniący obowiązki',
    'RP': 'Rzeczpospolita Polska',
    's.': 'strona',
    'S.A.': 'spółka akcyjna',
    'str.': 'strona',
    'św.': 'święty, święta',
    'tj.': 'to jest',
    'tzn.': 'to znaczy',
    'tzw.': 'tak zwany',
    'ub.': 'ubiegły',
    'UE': 'Unia Europejska',
    'ul.': 'ulica',
    'wf': 'wychowanie fizyczne',
    'wsch.': 'wschodni, wschód',
    'zach.': 'zachodni, zachód',
    'zob.': 'zobacz'
}

# 3
games = {1: 'TF2', 2: 'CS:GO', 3: 'GTA V'}
n_1 = len(games)

# 4
sentence = input('Wpisz zdanie\n')
n_2 = sentence[:sentence.index('.')].count('a')

# 5
stdout.writelines('Podaj 3 liczby całkowite\n')
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
n_3 = a ** b + c

# 6
a = int(input('Podaj liczbę całkowitą: '))
b = int(input('Podaj liczbę całkowitą: '))
c = int(input('Podaj liczbę całkowitą: '))

if a >= b:
    if a >= c:
        print('Największą liczbą jest', a)

    else:
        print('Największą liczbą jest', c)

elif b >= c:
    print('Największą liczbą jest', b)

else:
    print('Największą liczbą jest', c)

# 7
numbers = [9.5, 0.95, 5, 7, 0.86, 3, 7, 9, 1, 0.2]

for i, n in enumerate(numbers):
    numbers[i] = n ** 2

# 8
i = 1
li = []

while i <= 10:
    x = int(input('Podaj liczbę\n'))

    if not x & 1:
        li.append(x)

    i += 1

# 9
s = True
letter = []

for x in range(5):
    if s:
        letter.append('EEEEEE\n')
        s = False

    else:
        letter.append('E\n')
        s = True

print(''.join(letter))

# 10
n_3 = float(input('Podaj liczbę\n'))

if n_3 < 0:
    print('Brak rozwiązań w zbiorze liczb rzeczywistych')

else:
    print(math.sqrt(n_3))

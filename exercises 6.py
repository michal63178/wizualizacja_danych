import numpy

# 1
array_1 = numpy.arange(4, 84, 4)

# 2
array_2 = numpy.arange(10, dtype='float')
array_3 = array_2.astype(dtype='int64')


# 3
def function_1(n):
    return numpy.arange(1, n ** 2 + 1).reshape(n, n)


# 4
def function_2(n, m):
    return numpy.logspace(1, m, num=m, base=n)


# 5
def function_3(vector):
    return numpy.diag(numpy.arange(vector, 0, -1))


# 6
word = 'słowo'
array_4 = numpy.diag(list(f'{word[::-1]} '))
li = [array_4[0, 0]]
li.extend([letter for letter in word])
array_4[0] = li
array_4[1:, 0] = [letter for letter in word]
print(array_4)


# 7
def function_4(n):
    array_5 = numpy.diag([2] * n)
    index = 1
    term = 4
    x = 0
    y = 1

    for j in range(n - 1, 0, -1):
        for k in range(j, 0, -1):
            array_5[x, y] = term
            x += 1
            y += 1

        term += 2
        index += 1
        x = 0
        y = index

    term = 4
    index = -2
    x = -1
    y = -2

    for j in range(n - 1, 0, -1):
        for k in range(j, 0, -1):
            array_5[x, y] = term
            x -= 1
            y -= 1

        term += 2
        index -= 1
        x = -1
        y = index

    return array_5


# 8
def function_5(array, vertically):
    if vertically:
        if len(array.shape) == 1:
            if not array.shape[0] & 1:
                return array.reshape((2, array.shape[0] // 2))

            else:
                return 'Zła liczba kolumn'

        else:
            if not array.shape[1] & 1:
                return numpy.array([array[:, :array.shape[1] // 2],
                                    array[:, array.shape[1] // 2:]])

            else:
                return 'Zła liczba kolumn'

    else:
        if len(array.shape) != 1 and not array.shape[0] & 1:
            return array.reshape((2, array.shape[0] // 2, array.shape[1]))

        else:
            return 'Zła liczba wierszy'


# 9
def arithmetic_progression(initial_term, common_difference):
    return [term for term in range(initial_term, initial_term + 25 *
                                   common_difference, common_difference)]


array_6 = numpy.array(arithmetic_progression(5, 5)).reshape((5, 5))

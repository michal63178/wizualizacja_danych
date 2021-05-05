import numpy

# 1
array_1 = numpy.arange(3)
array_2 = numpy.arange(4, 7)

print(array_1 * array_2)

# 2
array_3 = numpy.arange(9).reshape(3, 3)
array_4 = numpy.arange(16).reshape(4, 4)

print(array_3, array_3.min(axis=0), array_3.min(axis=1), '', array_4,
      array_4.min(axis=0), array_4.min(axis=1), sep='\n')

# 3
print(array_1.dot(array_2))

# 4
print(numpy.arange(4, 7) * numpy.exp(numpy.arange(3)))

# 5
a = numpy.sin(numpy.arange(6).reshape(3, 2))

# 6
b = numpy.cos(numpy.arange(6).reshape(3, 2))

# 7
print(a + b)

# 8
li_1 = []
array_6 = numpy.arange(9).reshape(3, 3)

for row in array_6:
    li_1.append(f'{row}\n')

print(''.join(li_1))

# 9
li_2 = []
array_7 = numpy.arange(9).reshape(3, 3).flat

for element in array_7:
    li_2.append(f'{element}')

print(', '.join(li_2))

# 10
array_8 = numpy.arange(81).reshape(9, 9)
print(array_8, end='\n\n')
print(array_8.reshape(1, 81), end='\n\n')
print(array_8.reshape(3, 27), end='\n\n')
print(array_8.reshape(27, 3), end='\n\n')
print(array_8.reshape(81, 1), end='\n\n')

# 11
array_9 = numpy.arange(12)
print(array_9, end='\n\n\n')
print(array_9.reshape(3, 4), array_9.reshape(3, 4).ravel(),
      sep='\n\n', end='\n\n\n')
print(array_9.reshape(4, 3), array_9.reshape(4, 3).ravel(),
      sep='\n\n', end='\n\n\n')
print(array_9.reshape(2, 6), array_9.reshape(2, 6).ravel(),
      sep='\n\n', end='\n\n\n')

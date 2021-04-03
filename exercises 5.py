# 1


class Material:
    material_kind = None
    length = None
    width = None
    name = None

    def show_name(self):
        return self.name


class Clothes(Material):
    size = None
    color = None
    whose = None

    def show_clothes_info(self):
        return self.size, self.color, self.whose


class Sweater(Clothes):
    sweater_kind = None

    def show_sweater_info(self):
        return self.sweater_kind


Material.material_kind = 'bawełna'
Material.length = 4
Material.width = 8
Material.name = 'ubranie'

material = Material()
print(material.show_name())

Clothes.size = 'L'
Clothes.color = 'zielony'
Clothes.whose = 'Mariusz'

clothe = Clothes()
print(clothe.show_clothes_info(), clothe.show_name())

Sweater.sweater_kind = 'z golfem'

sweater = Sweater()
print(sweater.show_sweater_info(), clothe.show_clothes_info(),
      clothe.show_name())


# 2, 3


class Square:
    def __init__(self, side):
        self.side = side

    def __add__(self, other):
        return Square(5 * self.side)

    def __ge__(self, other):
        if self.side >= other.side:
            return 'Pierwszy jest nie mniejszy'

        else:
            return 'Pierwszy jest mniejszy'

    def __gt__(self, other):
        if self.side > other.side:
            return 'Pierwszy jest większy'

        else:
            return 'Pierwszy jest nie większy'

    def __le__(self, other):
        if self.side <= other.side:
            return 'Pierwszy jest nie większy'

        else:
            return 'Pierwszy jest większy'

    def __lt__(self, other):
        if self.side < other.side:
            return 'Pierwszy jest mniejszy'

        else:
            return 'Pierwszy jest nie mniejszy'


square_1 = Square(2)
print(square_1.side)
square_2 = Square(5) + square_1
print(square_2.side)
print(square_1 >= square_2)
print(square_1 > square_2)
print(square_1 <= square_2)
print(square_1 < square_2)


# 4


class Point:
    counter = 0


print(Point.counter)
obj_1 = Point()
print(obj_1.counter)
obj_1.counter += 1
print(obj_1.counter)
print(Point.counter)
Point.counter = 5
print(Point.counter)
print(obj_1.counter)
obj_2 = Point()
obj_2.counter = 2
print(Point.counter)
print(obj_1.counter)
print(obj_2.counter)


# 5


class Person:
    pass


class Employee(Person):
    pass


class Manager(Employee):
    pass


employee = Employee()
manager = Manager()
print(isinstance(employee, Employee), isinstance(manager, Manager),
      issubclass(Employee, Person),
      issubclass(Manager, Employee))


# 6, 7


class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.len = len(collection)

    def __iter__(self):
        self.i = 0

        return self

    def __next__(self):
        if not self.i & 1:
            index = self.i
            self.i += 1

            return self.collection[index]

        else:
            self.i += 1


iterator_1 = iter(Iterator(range(10)))
iterator_2 = iter(Iterator('qwerty'))
iterator_3 = iter(Iterator([1, .4, 'a', []]))

for element in range(10):
    e = next(iterator_1)

    if e is not None:
        print(e)

print()

for element in range(6):
    e = next(iterator_2)

    if e is not None:
        print(e)

print()

for element in range(4):
    e = next(iterator_3)

    if e is not None:
        print(e)


# 8


class Vowels:
    vowels = 'aąeęiouy'

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        self.i = 0

        return self

    def __next__(self):
        if self.text[self.i] in Vowels.vowels:
            index = self.i
            self.i += 1

            return self.text[index]

        else:
            self.i += 1


# 9


def generator(text):
    vows = 'aąeęiouy'

    for letter in text:
        if letter in vows:
            yield letter


# 10


def arithmetic_progression(initial_term, common_difference):
    while True:
        yield initial_term
        initial_term += common_difference

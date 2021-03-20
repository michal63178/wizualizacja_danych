from random import randint


def open_file(name):
    with open(name, encoding='utf8') as f:
        return f.read()


def save_file(name, content):
    with open(name, 'w', encoding='utf8') as f:
        f.write(content)


# 1
numbers = f'{[randint(0, 30) for number in range(10)]}' \
              .replace(', ', '\n')[1:-1]
save_file('numbers.txt', numbers)

# 2
print(open_file('numbers.txt'), end='\n\n')

# 3
save_file('text.txt', 'lorem ipsum\n' * 10)
print(open_file('text.txt'), end='\n\n')


# 4


class Shopping:
    def __init__(self, name, quantity, unit_of_measurement, unit_price):
        self.product_name = name
        self.quantity = quantity
        self.unit_of_measurement = unit_of_measurement
        self.unit_price = unit_price

    def about_product(self):
        print(f'Nazwa produktu: {self.product_name}\n'
              f'Ilość: {self.quantity}\n'
              f'Jednostka miary: {self.unit_of_measurement}\n'
              f'Cena za jednostkę: {self.unit_price} zł')

    def product_quantity(self):
        return f'{self.quantity} {self.unit_of_measurement}'

    def product_cost(self):
        return f'{self.quantity * self.unit_price} zł'


# 5


class ArithmeticProgression:
    progression = []
    initial_term = 0
    common_difference = 0
    number_of_terms = 0

    def get_parameters(self, initial_term, common_difference, number_of_terms):
        self.__class__.initial_term = initial_term
        self.__class__.common_difference = common_difference
        self.__class__.number_of_terms = number_of_terms

    def create_progression(self):
        last_term = self.__class__.initial_term \
                    + self.__class__.common_difference \
                    * (self.__class__.number_of_terms - 1)
        self.__class__.progression.clear()
        self.__class__.progression.extend(
            [a_n for a_n in range(self.__class__.initial_term, last_term + 1,
                                  self.__class__.common_difference)])

    def progression_sum(self):
        return self.__class__.number_of_terms \
               * (2 * self.__class__.initial_term
                  + self.__class__.common_difference
                  * (self.__class__.number_of_terms - 1)) / 2

    def get_n_th_term(self, *args):
        return f'{[self.__class__.progression[term - 1] for term in args]}' \
               f''.replace(', ', '\n')[1:-1]

    def show_progression(self):
        print(f'{self.__class__.progression}'[1:-1], end='\n\n')


progression = ArithmeticProgression()
progression.get_parameters(0, 2, 10)
progression.create_progression()
print(progression.progression_sum())
print(progression.get_n_th_term(1, 5, 10))
progression.show_progression()


# 6


class Worm:
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step

    def go_up(self):
        self.y += self.step

    def go_down(self):
        self.y -= self.step

    def go_left(self):
        self.x -= self.step

    def go_right(self):
        self.x += self.step

    def show_position(self):
        print(f'x = {self.x}, y = {self.y}')


worm = Worm(0, 0, 1)
worm.go_up()
worm.go_down()
worm.go_left()
worm.go_right()
worm.show_position()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

num1 =  my_favorite_movies [0:10]
num_end = my_favorite_movies [42:57]
num2 = my_favorite_movies [12:25]
num4 = my_favorite_movies [35:40]
print(num1, num_end, num2, num4)
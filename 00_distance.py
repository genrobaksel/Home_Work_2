#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict ()

m = sites['Moscow']
l = sites['London']
p = sites['Paris']

Moscow_London_distance = ((m[0] - l[0]) ** 2 + (m[1] - l[1]) ** 2) ** .5
Moscow_Paris_distance = ((m[0] - p[0]) ** 2 + (m[1] - p[1]) ** 2) ** .5
London_Moscow_distance = ((m[0] - l[0]) ** 2 + (m[1] - l[1]) ** 2) ** .5
London_Paris_distance = ((l[0] - p[0]) ** 2 + (l[1] - p[1]) ** 2) ** .5
Paris_Moscow_distance = ((m[0] - p[0]) ** 2 + (m[1] - p[1]) ** 2) ** .5
Paris_London_distance = ((l[0] - p[0]) ** 2 + (l[1] - p[1]) ** 2) ** .5

distances ['Moscow'] = {}
distances ['Moscow']['London'] = Moscow_London_distance
distances ['Moscow']['Paris'] = Moscow_Paris_distance

distances ['London'] = {}
distances ['London']['Moscow'] = London_Moscow_distance
distances ['London']['Paris'] = London_Paris_distance

distances ['Paris'] = {}
distances ['Paris']['Moscow'] = Paris_Moscow_distance
distances ['Paris']['London'] = Paris_London_distance

print(distances)





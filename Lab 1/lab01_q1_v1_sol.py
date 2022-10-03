# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 04:13:46 2022

"""

PI = 3.14

radius = float(input('Enter radius: '))

square_area = (2 * radius) ** 2
circle_area = PI * radius ** 2
shaded_area = square_area - circle_area

print(f'Shaded area for a radius of {radius} is {shaded_area:.2f}')

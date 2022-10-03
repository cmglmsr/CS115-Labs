# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 04:13:46 2022

"""

# Input data
magnitude = float(input('Enter magnitude of earthquake: '))

category = ""
if magnitude < 3:
    category = "micro"
elif magnitude < 4:
    category = "minor"
elif magnitude < 5:
    category = "light"
elif magnitude < 6:
    category = "moderate"
elif magnitude < 7:
    category = "strong"
elif magnitude < 8:
    category = "major"
else:
    category = "great"

print("According to Richter scale")
print(f"\t{magnitude:.2f} magnitude refers to a {category} earthquake")
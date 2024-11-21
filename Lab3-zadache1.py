#оушен
#нбибд-01-24
#лаб 3 билет 11
# python

import math

def zodiac_year(year):
    if year < 1984:
        return "invalid year"

    diff = year - 1984
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    colors = ["Green", "Red"]

    animal = animals[diff % 12]
    color = colors[diff % 2]

    return f"The year {year} is the year of the {color} {animal}."

year = int(input())
print(zodiac_year(year))

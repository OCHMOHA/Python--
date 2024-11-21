#оушен
#нбибд-01-24
#лаб 3 билет 11
# python
#задача 1

import math

def zodiac_year(year):

    color = ["Green","Red","Yellow","White","Black"]
    
    animal = ["Rat","Cow","Tiger","Hare","Dragon","Snake","Horse","Sheep","Monkey","Chicken","Dog","Pig"]
    
    try:
    
        year = int(year)
        
        if year < 0:
            
            return "Invalid year"
            
        color = color [color_index]
        
        animal = animal[animal_index]
        
        animal_index = (year - 4) % 12
        
        color_index = (year - 4) % 10 % 2
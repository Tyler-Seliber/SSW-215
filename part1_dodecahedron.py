# Part 1

import random

def roll_dodecahedron():
    dodecahedron = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return dodecahedron[random.randint(1,12) - 1]
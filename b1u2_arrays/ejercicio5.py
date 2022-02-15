# vector con números aleatorios y ordenamiento

from random import *

vector = list()

for i in range(10):
    vector.append(randint(0,100))
vector.sort()

print(vector)
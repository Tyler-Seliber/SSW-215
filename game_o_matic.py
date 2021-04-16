import random

rand_numbers = []
dodecahedron_results = [0] * 12

print(dodecahedron_results)

for i in range(0,10000):
    r = random.randint(1,12)
    rand_numbers.append(r)
    dodecahedron_results[r-1] += 1

print(dodecahedron_results)
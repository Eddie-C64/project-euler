import numpy as np

n = 1000

m, r = 3, 5

sums = []

for number in range(n):
    if number % 5 ==0 or number % 3 == 0:
        sums.append(number)

print(len(sums))
print(sums)
print(sum(sums))

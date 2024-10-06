import math
summ = 0
for i in range(35, 111113+22, 22):
    cos_value = math.cos(math.radians(i))
    summ += cos_value
print(summ)
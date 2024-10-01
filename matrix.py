import random
x = int(input())
y = int(input())

matrix = [[random.randint(1,10)for i in range(x)] for j in range(y)]
for row in matrix:
    for element in row:
        print(element, end='\t')
    print()
print()
for i in range(len(matrix)):
    sub = matrix[i][i]
    matrix[i][i] = matrix[i][x-i-1]
    matrix[i][x-i-1] = sub

for row in matrix:
    for element in row:
        print(element, end='\t')
    print()

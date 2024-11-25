import random
def print_matrix(text, matrix_):
    print(text)
    for i in range(len(matrix_)):
        for j in range(len(matrix_[i])):
            print(matrix_[i][j], end="\t")
        print()

x, y = int(input()), int(input())
matrix = [[random.randint(0, x*y-x*y//3) for i in range(x)] for j in range(y)]
lst = []
dct = {}
print_matrix("Исходная матрица:", matrix)

for i in matrix:
    for j in i:
        lst.append(j)
for i in lst:
    dct[i] = lst.count(i)

keys = list(dct.keys())
values = list(dct.values())
unic = values.count(1)
no_unic = len(values) - unic

for i in range(len(keys)):
    if values[i] == 1:
        print(f"Элемент {keys[i]} - уникальный")
print()
for i in range(len(keys)):
    if values[i] != 1:
        print(f"Элемент {keys[i]} - {values[i]} повторов")

print()
print(f"Кол-во уникальных: {unic}")
print(f"Кол-во повторяющихся: {no_unic}")
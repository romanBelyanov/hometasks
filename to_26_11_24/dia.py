import random
def print_matrix(text, matrix_):
    print(text)
    for i in range(len(matrix_)):
        for j in range(len(matrix_[i])):
            print(matrix_[i][j], end="\t")
        print()

x = int(input())
dia1 = 1
dia2 = 1
matrix = [[random.randint(0, x*x//3) for i in range(x)] for j in range(x)]
print_matrix("Исходная матрица:", matrix)

for i in range(1, x+1):
    for j in range(1, x+1):
        if i == j:
            dia1 *= matrix[i-1][j-1]
        if j == x - i + 1:
            dia2 *= matrix[i-1][j-1]

print(f"Произведение элементов первой диагонали: {dia1}")
print(f"Произведение элементов второй диагонали: {dia2}")
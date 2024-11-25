import random
def tr_mat(matrix_):
    matrix_ = [[matrix_[j][i] for j in range(len(matrix_))] for i in range(len(matrix_[0]))]
    return matrix_
def print_matrix(text, matrix_):
    print(text)
    for i in range(len(matrix_)):
        for j in range(len(matrix_[i])):
            print(matrix_[i][j], end="\t")
        print()

x, y = int(input()), int(input())
matrix = [[random.randint(0, 2*x*y) for i in range(x)] for j in range(y)]

print_matrix("Изначальная матрица:", matrix)
print_matrix("Конечная матрица:", tr_mat(matrix))
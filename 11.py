A = 0
H = 0
R = 0
M = 0
PI = 3.14159
def trying():
    try:
        global A, H, R, M
        A = int(input("Введите ребро кубической ёмкости: "))
        H = int(input("Введите высоту цилиндра: "))
        R = int(input("Введите радиус основания цилиндра: "))
        M  = int(input("Введите объём жидкости: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(A, H, R, M):
    if A**3 >= M:
        print("Поместится в первую ёмкость")
    else:
        print("Не поместится в первую ёмкость")
    if PI * R**2 * H >= M:
        print("Поместится во вторую ёмкость")
    else:
        print("Не поместится во вторую ёмкость")
    if A**3 + PI * R**2 * H >= M:
        print("Поместится в обе ёмкости")
    else:
        print("Не поместится в обе ёмкости")


if __name__ == "__main__":
    trying()
    main(A, H, R, M)
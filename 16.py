A = 0
B = 0
C = 0
def trying():
    try:
        global A, B, C
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        C = int(input("Введите число C: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(A, B, C):
    if A < B:
        print("Выполняется неравенство A<B")
    if B >= C:
        print("Выполняется неравенство B >= C")
    if not A < B and not B >= C:
        print("Не выполняется ни одно из неравенств")


if __name__ == "__main__":
    trying()
    main(A, B, C)
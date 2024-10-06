A = 0
B = 0
C = 0
M = 0
K = 0
def trying():
    try:
        global A, B, C, M, K
        A = int(input("Введите длину коробки: "))
        B = int(input("Введите ширину коробки: "))
        C = int(input("Введите высоту коробки: "))
        M = int(input("Введите высоту двери: "))
        K = int(input("Введите ширину двери: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(A, B, C, M, K):
    if (A <= M and B <= K) or (B <= M and A <= K) or (C <= M and B <= K) or (B <= M and C <= K) or (A <= M and C <= K) or (C <= M and A <= K):
        print("Коробка пройдёт в дверь")
    else:
        print("Коробка не пройдёт в дверь")


if __name__ == "__main__":
    trying()
    main(A, B, C, M, K)
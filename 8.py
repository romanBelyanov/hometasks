S = 0
R = 0
K = 0
def trying():
    try:
        global S, R, K
        S = int(input("Введите площадь зала: "))
        R = int(input("Введите радиус сцены: "))
        K = int(input("Введите расстояние от сцены до стены: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(S, R, K):
    if S / 4 >= R+K:
        print("Можно поместить")
    else:
        print("Нельзя поместить")


if __name__ == "__main__":
    trying()
    main(S, R, K)
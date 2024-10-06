X = 0
Y = 0
def trying():
    try:
        global X, Y
        X = float(input("Введите число X: "))
        Y = float(input("Введите число Y: "))
        if X == 0 or Y == 0:
            1/0
    except:
        print("Нужно вводить ненулевые числа")
        trying()

def main(X, Y):
    print(f"Z={1/(X*Y)}")


if __name__ == "__main__":
    trying()
    main(X, Y)
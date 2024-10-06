n = 0
def trying():
    try:
        global n
        n = int(input("Введите число: "))
    except:
        print("Нужно вводить целое число")
        trying()

def main(n):
    for i in range(1, 4):
        for j in range(i*n):
            print(i, end=" ")
        print()


if __name__ == "__main__":
    trying()
    main(n)
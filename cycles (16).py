n = 0
a = 0
def trying():
    try:
        global n, a
        a = int(input("Введите число a: "))
        n = int(input("Введите число n: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(a, n):
    summ = 0
    for i in range(1, n+1):
        summ += (a+i)**2
        print(summ)
    print(summ)


if __name__ == "__main__":
    trying()
    main(a, n)
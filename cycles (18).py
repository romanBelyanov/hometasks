n = 0
def trying():
    try:
        global n
        n = int(input("Введите число: "))
    except:
        print("Нужно вводить целое число")
        trying()

def main(n):
    summ = 0
    proiz = 1
    for i in range(1, n+1):
        for j in range(i, 2*i+1):
            proiz *= j
        summ += proiz
        proiz = 1
    print(summ)


if __name__ == "__main__":
    trying()
    main(n)
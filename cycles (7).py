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
    for i in range(1, n+1):
        summ += i
    print(summ)


if __name__ == "__main__":
    trying()
    main(n)
import math
n = 0
x = 0
def trying():
    try:
        global n, x
        x = int(input("Введите число x: "))
        n = int(input("Введите число n: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(x, n):
    summ = 0
    for i in range(1, n+1):
        cos_value = math.cos(math.radians(x**i))
        summ += cos_value
    print(summ)


if __name__ == "__main__":
    trying()
    main(x, n)
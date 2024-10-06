num1 = 0
def trying():
    try:
        global num1
        num1 = int(input("Введите число для проверки его знака: "))
    except:
        print("Нужно вводить целое число")
        trying()

def main(num):
    if num > 0:
        print(f"Число {num} больше нуля (положительное)")
    elif num < 0:
        print(f"Число {num} меньше нуля (отрицательное)")
    else:
        print("Это число нуль")


if __name__ == "__main__":
    trying()
    main(num1)
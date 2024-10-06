num1 = 0
def trying():
    try:
        global num1
        num1 = int(input("Введите число для проверки его четности и кратности 7: "))
    except:
        print("Нужно вводить целое число")
        trying()

def main(num):
    if num % 2 == 0:
        print(f"Число {num} четное")
    else:
        print(f"Число {num} нечетное")
    if num % 7 == 0:
        print(f"Число {num} делится на 7")
    else:
        print(f"Число {num} не делится на 7")


if __name__ == "__main__":
    trying()
    main(num1)
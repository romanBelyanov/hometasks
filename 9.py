num1 = 0
def trying():
    try:
        global num1
        num1 = int(input("Введите номер места: "))
        if num1 < 1 or num1 > 54:
            1/0
    except:
        print("Нужно вводить целое число от 1 до 54")
        trying()

def main(num):
    if num % 2 == 0:
        print(f"Место номер {num} находится сверху")
    else:
        print(f"Место номер {num} находится снизу")
    if 1 <= num <= 36:
        print(f"Место номер {num} находится в купе")
    else:
        print(f"Место номер {num} - боковое")


if __name__ == "__main__":
    trying()
    main(num1)
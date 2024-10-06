num1 = 0
def trying():
    try:
        global num1
        num1 = int(input("Введите курс доллара: "))
    except:
        print("Нужно вводить целое число")
        trying()

def main(num):
    for i in range(1, 101):
        print(f"{i}$ - {i*num} рублей - {i*num/20} кг")


if __name__ == "__main__":
    trying()
    main(num1)
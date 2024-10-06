num1 = 0
def trying():
    try:
        global num1
        num1 = int(input("Введите денежную сумму: "))
        if num1 < 0:
            1/0
    except:
        print("Нужно вводить целое неотрицательное число")
        trying()

def main(num):
    five_hundred = 0
    hundred = 0
    ten = 0
    two = 0
    if num % 2 == 0:
        while num > 0:
            while num > 500:
                five_hundred += 1
                num -= 500
            while num > 100:
                hundred += 1
                num -= 100
            while num > 10:
                ten += 1
                num -= 10
            while num > 0:
                two += 1
                num -= 2
        print(f"{five_hundred} купюр по 500 рублей,\n{hundred} купюр по 100 рублей,\n{ten} купюр по 10 рублей,\n{two} монет по 2 рубля")
    else:
        print(f"Нельзя разменять сумму {num} рублей купюрами 500, 100, 10 рублей и монетой 2 рубля")


if __name__ == "__main__":
    trying()
    main(num1)
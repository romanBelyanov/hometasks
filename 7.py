num1 = 0
side = 0
def trying():
    try:
        global num1, side
        num1 = eval(input("Введите диаметр бруса: "))
        side = eval(input("Введите сторону квадратного бруса: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(D, side):
    if (2 * side ** 2)**0.5 <= D:
        print("Можно выпилить")
    else:
        print("Нельзя выпилить")

if __name__ == "__main__":
    trying()
    main(num1, side)
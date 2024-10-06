X = 0
a = 0
b = 0
def trying():
    try:
        global X, a, b
        X = float(input("Введите число: "))
        a = float(input("Введите начало промежутка: "))
        b = float(input("Введите конец промежутка: "))
    except:
        print("Нужно вводить числа")
        trying()

def main(X, a, b):
    if a <= X <= b or a >= X >= b:
        print(f"Число {X} находится в промежутке от {a} до {b}")
    else:
        print(f"Число {X} не находится в промежутке от {a} до {b}")


if __name__ == "__main__":
    trying()
    main(X, a, b)
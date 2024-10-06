a = 0
b = 0
c = 0
d = 0
def trying():
    try:
        global a, b, c, d
        a = int(input("Введите длину первого прямоугольника: "))
        b = int(input("Введите ширину первого прямоугольника: "))
        c = int(input("Введите длину второго прямоугольника: "))
        d  = int(input("Введите ширину второго прямоугольника: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(a, b, c, d):
    if a <= c and b <= d or a <= d and b <= c:
        print(f"Прямоугольник {a}x{b} поместится в прямоугольник {c}x{d}")
    else:
        print(f"Прямоугольник {a}x{b} не поместится в прямоугольник {c}x{d}")

if __name__ == "__main__":
    trying()
    main(a, b, c, d)
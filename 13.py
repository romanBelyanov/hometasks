side1 = 0
side2 = 0
side3 = 0
def trying():
    try:
        global side1, side2, side3
        side1 = int(input("Введите первую сторону треугольника: "))
        side2 = int(input("Введите вторую сторону треугольника: "))
        side3 = int(input("Введите третью сторону треугольника: "))
    except:
        print("Нужно вводить целые числа")
        trying()

def main(A, B, C):
    if A + B > C or A + C > B or B + C > A:
        print(f"Треугольник со сторонами {A}, {B}, {C} существует")
    else:
        print(f"Треугольника со сторонами {A}, {B}, {C} не существует")


if __name__ == "__main__":
    trying()
    main(side1, side2, side3)
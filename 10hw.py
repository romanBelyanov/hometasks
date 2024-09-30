num1 = 0
num2 = 0
num3 = 0
res = 0
def trying():
	global num1, num2, num3
	try:
		num1 = int(input("Введите первое число для сравнения: "))
		num2 = int(input("Введите второе число для сравнения: "))
		num3 = int(input("Введите третье число для сравнения: "))
	except:
		print("Нужно вводить числа")
		trying()
trying()
if num1 >= num2:
    if num2 >= num3:
        res = num1
    else:
        if num1 >= num3:
            res = num1
        else:
            res = num3
else:
    if num2 >= num3:
        res = num2
    else:
        if num2 >= num3:
            res = num2
        else:
            res = num3
print(f"Наибольшее число - {res}")
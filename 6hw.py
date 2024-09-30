num1 = 0
num2 = 0
num3 = 0
def trying():
	global num1, num2, num3
	try:
		num1 = int(input("Введите первое число для проверки его четности: "))
		num2 = int(input("Введите второе число для проверки его четности: "))
		num3 = int(input("Введите третье число для проверки его четности: "))
	except:
		print("Нужно вводить числа")
		trying()
trying()
if num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0:
	print("Хотя бы одно из трех чисел четно")
else:
	print("Четных нет")
num1 = 0
num2 = 0
def trying():
	global num1, num2
	try:
		num1 = int(input("Введите первое число для сравнения его с 10: "))
		num2 = int(input("Введите второе число для сравнения его с 10: "))
	except:
		print("Нужно вводить числа")
		trying()
trying()
if num1 > 10 and num2 > 10:
	print("Оба числа больше 10")
elif num1 > 10 and num2 <= 10:	
	print("Первое число больше 10, второе число меньше либо равно 10")
elif num2 > 10 and num1 <= 10:	
	print("Первое число меньше либо равно 10, второе число больше 10")
else:
	print("Оба числа меньше либо равны 10")
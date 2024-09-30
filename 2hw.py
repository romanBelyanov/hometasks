num = 0
def trying():
	global num
	try:
		num = int(input("Введите число для проверки его чётности: "))
	except:
		print("Нужно вводить число")
		trying()
trying()
if num % 2 == 0:
	print("Число чётное")
elif num % 2 != 0:
	print("Число нечётное")
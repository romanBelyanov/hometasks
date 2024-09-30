num = 0
def trying():
	global num
	try:
		num = int(input("Введите число для проверки его знака: "))
	except:
		print("Нужно вводить число")
		trying()
trying()
if num > 0:
	print("Число положительное")

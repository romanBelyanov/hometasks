num = 0
def trying():
	global num
	try:
		num = int(input("Введите число для проверки его наличия в диапазоне от 10 до 20 включительно: "))
	except:
		print("Нужно вводить число")
		trying()
trying()
if 10 <= num <= 20:
	print("Число находится в диапазоне от 10 до 20 включительно")
elif not(10 <= num <= 20):
	print("Число не находится в диапазоне от 10 до 20 включительно")
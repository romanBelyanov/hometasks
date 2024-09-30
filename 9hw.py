num = 0
def trying():
	global num
	try:
		num = int(input("Введите год для проверки его на високосность: "))
	except:
		print("Нужно вводить число")
		trying()
trying()
if num % 4 == 0 and not num % 100 == 0 or num % 400 == 0:
	print("Год високосный")
else:
	print("Год невисокосный")
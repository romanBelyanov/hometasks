num = 0
def trying():
	global num
	try:
		num = int(input("Введите число: "))
	except:
		print("Нужно вводить число")
		trying()
trying()
if num < 10:
	print("Меньше 10")
elif 10 <= num <= 20:
	print("Между 10 и 20")
else:
	print("Больше 20")
password1 = ""
password2 = ""
def trying():
	global password1, password2
	try:
		password1 = int(input("Введите пароль: "))
		password2 = int(input("Повторите пароль: "))
	except:
		print("Нужно вводить пароли")
		trying()
trying()
if password1 == password2:
	print("Доступ разрешен")
else:
	print("Доступ запрещен")
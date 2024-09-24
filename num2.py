alphabet, strs, letters, pages = 0, 0, 0, 0
def trying():
    try:
        global alphabet, strs, letters, pages
        alphabet = int(input("Сколько символов в алфавите? "))  # 32
        strs = int(input("Сколько строк на странице? "))  # 64
        letters = int(input("Сколько символов в строке? "))  # 112
        pages = int(input("На скольки сторонах листа есть печать? (1, 2) "))
        if pages not in [1, 2]:
            1/0  # Если кто-то хочет написать на 3 сторонах листа, это вернет его обратно на ввод
    except:
        print("Вводите цифры")
trying()
bytes_for_symbol = 0
for i in range(1, alphabet // 2 + 1):
    if 2 ** i >= alphabet:
        bytes_for_symbol = i  # Вычисление кол-ва битов для кодирования одного символа
        break

bytes_on_page = strs * letters * pages * bytes_for_symbol  # Вычисление кол-ва битов для кодирования всего текста символа
print(f"{bytes_on_page} битов")
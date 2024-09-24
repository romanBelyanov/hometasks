# Белянов Роман Антонович, ИИ-71, уровень С
memory, memory_num, memory_what_in = "", "", ""
def trying():
    global memory, memory_num, memory_what_in
    try:
        memory = int(input("Введите память устройства в Кб (указывайте только число): "))  # Вводить надо только число: 8
    except:
        print("Пожалуйста, введите только число")
        trying()

trying()

print(f"{memory} Кб = {memory / 1024} Мб = {memory * 1024} байт = {memory * 1024 * 8} бит")



km = 10
summ = 0
for i in range(10):
    if i <= 6:
        summ += km
    km = km / 100 * 110
    print(f"Пробежал за {i+1} день тренировок {km} км")
print(f"Пробежал за 7 дней {summ} км")
n = 0
def trying():
    try:
        global n
        n = int(input("Введите число: "))
    except:
        print("Нужно вводить целое число")
        trying()
trying()
summ1 = 0
km = 10
for i in range(n):
    summ1 += km
    km = km / 100 * 110
print(f"Пробежал за {n} дней {summ1} км")
summ2 = 0
km = 10
for i in range(n):
    summ2 += km
    if summ2 > 80:
        summ2 -= km
        res = i
        break
    km = km / 100 * 110
print(f"Нужно остановиться на {res} дне")

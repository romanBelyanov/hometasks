summ = 0
for i in range(1, 100+1):
    for j in range(1, i+1):
        summ += j
    print(summ)
    summ = 0
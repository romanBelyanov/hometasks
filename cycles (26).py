i = 0
run = True
while run:
    if i % 2 == 1 and i % 3 == 1 and i % 4 == 1 and i % 5 == 1 and i % 6 == 1 and i % 7 == 1 and i % 8 == 1 and i % 9 == 1 and i % 10 == 1 and i % 11 == 0:
        print(i)
        if i > 1000000:
            run = False
    i += 11
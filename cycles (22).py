for i in range(10000, 100000):
    one = int(str(i)[0])
    two = int(str(i)[1])
    three = int(str(i)[2])
    four = int(str(i)[3])
    five = int(str(i)[4])
    if i % 2 == 0 and int(str(i)[2]) % 2 == 1 and (one + two + three + four + five)  % 4 == 0:
        print(i, end=" ")
for i in range(1000, 10000):
    one = int(str(i)[0])
    two = int(str(i)[1])
    three = int(str(i)[2])
    four = int(str(i)[3])
    if 600 * (one + two + three + four) == i:
        print(i, end=" ")
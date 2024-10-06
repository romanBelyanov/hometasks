for i in range(100, 1000):
    one = int(str(i)[0])
    two = int(str(i)[1])
    three = int(str(i)[2])
    if one**3 + two**3 + three**3 == i:
        print(i, end=" ")
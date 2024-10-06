for i in range(1000, 10000):
    first = i // 1000
    second = (i//100) % 10
    third =  (i%100) // 10
    fourth = i % 10
    if first != second and first != third and first != fourth and second != third and second != fourth and third != fourth:
        print(i, end=" ")
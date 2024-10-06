
def main():
    summ = 0
    for i in range(10, 0, -1):
        for j in range(i):
            print(i, end="\t")
            summ += i
        print()
    print(summ)


if __name__ == "__main__":
    main()
def mundaneMath():
    a = []
    for i in range(1, 101):
        if (i % 2 == 0):
            a.append(i)
    x = sum(a)
    print(x)


if __name__ == "__main__":
    mundaneMath()

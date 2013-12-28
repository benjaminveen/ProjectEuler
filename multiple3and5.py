def multiple3and5():
    i = 3
    tot = 0
    for i in range (3,1000):
        if (i%3) == 0:
            tot+=i
        elif (i%5) == 0:
            tot+=i
    print(tot)

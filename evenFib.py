def evenFib():
    a = 1
    b = 2
    c = 0
    tot = 2
    while c <= 4000000:
        c = a+b
        a = b
        b = c
        print("Next Fib #: ",c)
        if (c%2) == 0:
            tot+=c
            print("Current total: ",tot)
    print(tot)

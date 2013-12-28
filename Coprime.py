from fractions import gcd

def modInverse(startRange,endRange):
    i = startRange
    sigma = 0
    for i in range (startRange,endRange+1):
        x = 1
        greatest = 0
        for x in range (1,i-1):
            if coprime(i,x):
                check = x*x
                check = check % i
                if check == 1:
                    if x > greatest:
                        greatest = x
            x+=1
        print("Greatestmod coprime to ",i,": ",greatest)
        i+=1
        sigma+=greatest
    print("The sum of all greatest coprimes such that m mod n = m is: ",sigma) 

def coprime(testNum,currNum):
    g = gcd(testNum,currNum)
    if g == 1:
        return True
    else:
        return False

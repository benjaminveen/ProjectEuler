from fractions import gcd

def largestPrimeFactor():
    toFactor = 600851475143
    factors = []
    tempFactor = 600851475143
    check1 = False
    while check1 == False:
        i = 2
        check = False
        while check == False:
            x = tempFactor%i
            if x == 0:
                factors.append(i)
                tempFactor = tempFactor/i
                print("Factor: ",i)
                check = True
            i+=1
        #if toFactor%tempFactor == 0:
            #check1 = True
    print(factors)
                
            
        

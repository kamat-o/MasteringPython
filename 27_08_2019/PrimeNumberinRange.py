def primeNumbersInRange(start,end):
    primes = []
    for i in range(start,end+1):
        # isprime = True
        for j in range(2,i):
            if (i%j==0):
                # isprime = False
                break
        else:
            primes.append(i)    
        # if isprime:
        #     primes.append(i)
    return primes

print(primeNumbersInRange(2,10))
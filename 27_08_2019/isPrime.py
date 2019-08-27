def isPrime(num):
    prime = False
    for j in range(2,num):
        if (num%j==0):
            break
    else:
        prime = True

    return prime

print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
print(isPrime(5))
print(isPrime(6))
import math

def SumOfSquares(n):
    result = 0
    for i in range(n+1):
        result += pow(i,2)

    return result

def SumOfSquares_2(n):
    return int((n*(n+1)*(2*n+1))/6)


print(SumOfSquares(4))
print(SumOfSquares_2(4))


#################################################

def SumofCubes(n):
    v = (n*(n+1)/2)
    return int(pow(v,2))

def SumofCubes_2(n):
    result = 0
    for i in range(n+1):
        result += pow(i,3)

    return result

print(SumofCubes(5))
print(SumofCubes_2(5))
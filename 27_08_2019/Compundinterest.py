import math

def compoundinterest(p,t,r):
    return p * (pow((1+(r/100)),t))

print(compoundinterest(1200,2,5.4))

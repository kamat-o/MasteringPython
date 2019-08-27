def isFibbonacci(n):
    fibb = [0,1]
    num1 = fibb[0]
    num2 = fibb[1]

    while(True):
        mysum = num1 + num2
        fibb.append(mysum)
        num1=num2
        num2=mysum
        if mysum >=n:
            break

    print(n in fibb)

isFibbonacci(0)
isFibbonacci(1)
isFibbonacci(8)
isFibbonacci(45)
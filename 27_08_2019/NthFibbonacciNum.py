def nThFibbonacciNumber(n):
    fibb = [0,1]
    num1 = fibb[0]
    num2 = fibb[1]
    for _ in range(2,n):
        sum = num1 + num2
        fibb.append(sum)
        num1=num2
        num2=sum

    print(fibb)
    print(fibb[n-1])

nThFibbonacciNumber(10)

# # Function for nth Fibonacci number 
  
# def Fibonacci(n): 
#     if n<0: 
#         print("Incorrect input") 
#     # First Fibonacci number is 0 
#     elif n==1: 
#         return 0
#     # Second Fibonacci number is 1 
#     elif n==2: 
#         return 1
#     else: 
#         return Fibonacci(n-1)+Fibonacci(n-2) 
  
# # Driver Program 
  
# print(Fibonacci(9)) 

#get the input from user
num = int(input("Enter the number to generate factorial : "))
result = 1
for i in (range(num,0,-1)):
    result*=i

print("Factorial of {0} is : {1}".format(num,result))


# def factorial(n): 
#     # single line to find factorial 
#     return 1 if (n==1 or n==0) else n * factorial(n - 1)
  
# # Driver Code 
# num = 5
# print("Factorial of",num,"is", factorial(num))
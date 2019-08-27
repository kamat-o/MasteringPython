import math

#get the number
num = input("Enter the number : ")

#get the length of the number
numlen = len(num)

result = 0
for i in range(numlen):
    result += pow(int(num[i]),numlen)

print(int(num)==result)


# def isArmstrong (x): 
#     n = len(str(x))
#     temp = x 
#     sum = 0
#     while (temp!=0): 
#         r = temp%10
#         print("reminder is {0}".format(r))
#         sum = sum + pow(r, n) 
#         temp = int(temp/10)
#         print("temp is {0}".format(temp))
  
#     # If condition satisfies 
#     return (sum == x) 

# print(isArmstrong(153))
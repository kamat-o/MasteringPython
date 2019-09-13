myList = [1,2,3,4,5,6]
# lstLen = len(myList)
myList[0],myList[-1] = myList[-1], myList[0]
print(myList)

# def swapList(list): 
      
#     # Storing the first and last element  
#     # as a pair in a tuple variable get 
#     get = list[-1], list[0] 
#     print(get)
#     # unpacking those elements 
#     list[0], list[-1] = get 
      
#     return list

# # Swap function 
# def swapList(list): 
      
#     start, *middle, end = list
#     list = [end, *middle, start] 
      
#     return list


# Swap function 
# def swapList(list): 
      
#     first = list.pop(0)    
#     last = list.pop(-1) 
      
#     list.insert(0, last)   
#     list.append(first)    
      
#     return list

# # Driver code 
# newList = [12, 35, 9, 56, 24] 
print(swapList(newList)) 


# Q: Given two lists, 1,2,3,4,5 and 2,3,1,0,5 
# find which numbers are not present in the second list.


list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
diff =set(list1)-set(list2)
print(diff)

# sum no:--

# list=[0,1,2,3,4,5,6]
# sum_list=0
# for i in list:
#         sum_list=sum_list+i
# print(sum_list) 


# x=[18,6,12,12,15,18,2,3,4,4]
# i=0
# b=[]
# while i<len(x):
#     if x[i] not in b:
#         b.append(x[i])
#     i=i+1
# print(b)

# a=[1,2,(3]
# b=[4,5,6]
# a.append(b)
# print(a)

# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)

# a=[1,2,3]
# a.pop(2)
# print(a)

# list=[]
# if list==[]:
#    print('Empty list')
# else:
#    print('List is not empty\n',list)

# list=[6,5,8,14,20,4,2]
# minimum=min(list)
# print(minimum)
# 
# 
x=int(input("enter the length..."))
a=[]
i=0
count=0
z=[]
while i<x:
    c=int(input("enter the number.."))
    a.append(c)
    if a[i] not in z:
        z.append(a[i])
    else:
        count+=1
    i=i+1
print(z)
print(count) 
       

    



























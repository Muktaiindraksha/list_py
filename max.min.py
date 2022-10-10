# find together maximum and minimum code in list.

a=[1,2,3,4,5]
i=0
max=0
min=a[i]
tmax=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]
    i+=1
print(max)
print(min)
   

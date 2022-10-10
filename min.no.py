# list=[6,5,8,14,20,4,2]
# minimum=min(list)
# print(minimum)

a=[6,5,8,14,20,4,2]
i=0
min=100
while i<len(a):
    if a[i]<min:     
        min=a[i]
    i=i+1
print(min)
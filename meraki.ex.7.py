elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# print("The original list is : " + str(elements))
odd_sum = 0
even_sum = 0
for a in elements:
    for b in str(a):
        if int(b)%2 == 0:
            even_sum+=int(b)
        else:
            odd_sum+=int(b)
print("Odd digit sum:" + str(odd_sum))
print("Even digit sum:" + str(even_sum))


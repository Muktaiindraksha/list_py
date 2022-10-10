# Write a code that works for any list, 
# it shows the two averages as the output. 
# One is the average of even numbers and 
# the other is the average of odd numbers from the given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sumeven=0
sumodd=0
for i in elements:
    if(i%2==0):
        sumeven+=i
else:
    sumodd+=i
print("Sum of even numbers is=",sumeven)
print("Sum of odd numbers is=",sumodd)





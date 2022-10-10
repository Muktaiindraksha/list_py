elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_count, odd_count = 0, 0
for num in elements:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


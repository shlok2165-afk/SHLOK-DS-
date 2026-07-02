
# numbers = [10, 20, 30, 40, 50]

# print(numbers)



numbers = []

numbers.append(5)
numbers.append(10)
numbers.append(15)
numbers.append(20)
numbers.append(25)

# Add +5 to every value
updated_list = []

for i in numbers:
    updated_list.append(i + 5)

print("Original List:", numbers)
print("After Adding 5:", updated_list)
# Different types of loops in Python

# 1. For loop with range
print("For loop with range:")
for i in range(5):
	print(f"Iteration {i}")

# 2. For loop with list
print("\nFor loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
	print(f"Current fruit: {fruit}")

# 3. While loop
print("\nWhile loop:")
count = 0
while count < 5:
	print(f"Count is: {count}")
	count += 1

# 4. Nested loop
print("\nNested loop:")
for i in range(3):
	for j in range(2):
		print(f"i = {i}, j = {j}")

# 5. Loop with else
print("\nLoop with else:")
for i in range(3):
	print(f"Inside loop: {i}")
else:
	print("Loop completed successfully")

# 6. Infinite loop with break
print("\nInfinite loop with break:")
counter = 0
while True:
	print(f"Counter: {counter}")
	counter += 1
	if counter >= 5:
		break

# 7. Loop with continue
print("\nLoop with continue:")
for i in range(5):
	if i == 2:
		continue
	print(f"Current number: {i}")

# 8. Enumerate in loop
print("\nEnumerate in loop:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
	print(f"Index {index}: {fruit}")

# 9. List comprehension (implicit loop)
print("\nList comprehension:")
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# 10. Dictionary comprehension
print("\nDictionary comprehension:")
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(f"Fruit lengths: {fruit_lengths}")

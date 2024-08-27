# Example of Python functions

# 1. Simple function with no parameters
def greet():
	print("Hello, World!")

# 2. Function with parameters
def greet_person(name):
	print(f"Hello, {name}!")

# 3. Function with default parameter
def greet_with_time(name, time="morning"):
	print(f"Good {time}, {name}!")

# 4. Function that returns a value
def add_numbers(a, b):
	return a + b

# 5. Function with multiple return values
def get_min_max(numbers):
	return min(numbers), max(numbers)

# 6. Function with arbitrary number of arguments
def sum_all(*args):
	return sum(args)

# 7. Function with keyword arguments
def person_info(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

# Example usage of the functions
greet()
greet_person("Alice")
greet_with_time("Bob")
greet_with_time("Charlie", "evening")

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

numbers = [1, 5, 3, 9, 2]
min_val, max_val = get_min_max(numbers)
print(f"Min: {min_val}, Max: {max_val}")

total = sum_all(1, 2, 3, 4, 5)
print(f"Sum of 1 to 5: {total}")

person_info(name="David", age=30, city="New York")

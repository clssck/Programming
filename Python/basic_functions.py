# Examples of basic Python functions

# 1. map() function
print("Example of map():")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# 2. filter() function
print("\nExample of filter():")
def is_even(n):
    return n % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(f"Original: {numbers}")
print(f"Even numbers: {even_numbers}")

# 3. sorted() function
print("\nExample of sorted():")
unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(unsorted_list)
print(f"Unsorted: {unsorted_list}")
print(f"Sorted: {sorted_list}")

# 4. zip() function
print("\nExample of zip():")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"Zipped: {zipped}")

# 5. enumerate() function
print("\nExample of enumerate():")
fruits = ["apple", "banana", "cherry"]
enumerated_fruits = list(enumerate(fruits, start=1))
print(f"Fruits: {fruits}")
print(f"Enumerated: {enumerated_fruits}")

# 6. any() and all() functions
print("\nExample of any() and all():")
bool_list = [True, False, True, True]
print(f"List: {bool_list}")
print(f"Any True? {any(bool_list)}")
print(f"All True? {all(bool_list)}")

# 7. reduce() function (from functools)
from functools import reduce
print("\nExample of reduce():")
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Numbers: {numbers}")
print(f"Product: {product}")

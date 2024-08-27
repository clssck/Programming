# Examples of match-case statements in Python

# 1. Basic match-case
def check_status(status):
	match status:
		case "online":
			print("The system is online")
		case "offline":
			print("The system is offline")
		case "maintenance":
			print("The system is under maintenance")
		case _:
			print("Unknown status")

print("Basic match-case:")
check_status("online")
check_status("maintenance")
check_status("error")

# 2. Match with multiple patterns
def describe_type(value):
	match value:
		case int() | float():
			print(f"{value} is a number")
		case str():
			print(f"{value} is a string")
		case list() | tuple() | set():
			print(f"{value} is a sequence")
		case _:
			print(f"{value} is of unknown type")

print("\nMatch with multiple patterns:")
describe_type(42)
describe_type("hello")
describe_type([1, 2, 3])

# 3. Match with conditions (guards)
def categorize_number(num):
	match num:
		case n if n < 0:
			print(f"{n} is negative")
		case 0:
			print("Zero")
		case n if n % 2 == 0:
			print(f"{n} is positive and even")
		case _:
			print(f"{n} is positive and odd")

print("\nMatch with conditions:")
categorize_number(-5)
categorize_number(0)
categorize_number(6)
categorize_number(7)

# 4. Match with destructuring
def analyze_point(point):
	match point:
		case (0, 0):
			print("Origin")
		case (0, y):
			print(f"Y-axis at y = {y}")
		case (x, 0):
			print(f"X-axis at x = {x}")
		case (x, y):
			print(f"Point at ({x}, {y})")
		case _:
			print("Not a valid point")

print("\nMatch with destructuring:")
analyze_point((0, 0))
analyze_point((0, 5))
analyze_point((3, 0))
analyze_point((2, 4))

# 5. Match with class patterns
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

def greet_person(person):
	match person:
		case Person(name=n, age=a) if a < 18:
			print(f"Hello, young {n}!")
		case Person(name=n, age=a) if a >= 65:
			print(f"Hello, respected elder {n}!")
		case Person(name=n):
			print(f"Hello, {n}!")
		case _:
			print("Hello, stranger!")

print("\nMatch with class patterns:")
greet_person(Person("Alice", 15))
greet_person(Person("Bob", 35))
greet_person(Person("Charlie", 70))
greet_person("Not a person")

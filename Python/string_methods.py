# Examples of Python string methods

# 1. upper() - Convert string to uppercase
text = "hello world"
print(text.upper())  # Output: HELLO WORLD

# 2. lower() - Convert string to lowercase
text = "HELLO WORLD"
print(text.lower())  # Output: hello world

# 3. capitalize() - Capitalize the first character
text = "hello world"
print(text.capitalize())  # Output: Hello world

# 4. strip() - Remove whitespace from both ends
text = "   hello world   "
print(text.strip())  # Output: hello world

# 5. replace() - Replace occurrences of a substring
text = "hello world"
print(text.replace("world", "python"))  # Output: hello python

# 6. split() - Split string into a list
text = "hello,world,python"
print(text.split(","))  # Output: ['hello', 'world', 'python']

# 7. join() - Join elements of an iterable into a string
words = ["hello", "world", "python"]
print(" ".join(words))  # Output: hello world python

# 8. startswith() - Check if string starts with a substring
text = "hello world"
print(text.startswith("hello"))  # Output: True

# 9. endswith() - Check if string ends with a substring
text = "hello world"
print(text.endswith("world"))  # Output: True

# 10. find() - Find the index of a substring
text = "hello world"
print(text.find("world"))  # Output: 6

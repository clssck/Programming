# Example using split() method in Python

# Original string
text = "apple,banana,cherry,date"

# Using split() to divide the string into a list
fruits = text.split(",")

# Print the resulting list
print("List of fruits:", fruits)

# Accessing individual elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Using split() with a different delimiter
sentence = "Python is awesome and powerful"
words = sentence.split(" ")
print("Words in the sentence:", words)

# Using split() with a limit
limited_split = sentence.split(" ", 2)
print("Limited split:", limited_split)

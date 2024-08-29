import re

# Regular expression examples in Python

# 1. Match a specific pattern
pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
print(match.group())  # Output: hello

# 2. Match digits
pattern = r"\d+"
text = "There are 123 apples and 456 oranges"
matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '456']

# 3. Match email addresses
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
text = "Contact us at info@example.com or support@company.co.uk"
matches = re.findall(pattern, text)
print(matches)  # Output: ['info@example.com', 'support@company.co.uk']

# 4. Replace using regex
pattern = r"(\d{3})-(\d{3})-(\d{4})"
text = "Call us at 123-456-7890 or 987-654-3210"
replaced = re.sub(pattern, r"(\1) \2-\3", text)
print(replaced)  # Output: Call us at (123) 456-7890 or (987) 654-3210

# 5. Split string using regex
pattern = r"[,;\s]+"
text = "apple,banana;  orange,grape"
split_result = re.split(pattern, text)
print(split_result)  # Output: ['apple', 'banana', 'orange', 'grape']

# 6. Match with optional group
pattern = r"colou?r"
print(re.match(pattern, "color"))  # Matches
print(re.match(pattern, "colour"))  # Matches

# 7. Match start and end of string
pattern = r"^start.*end$"
print(re.match(pattern, "start middle end"))  # Matches
print(re.match(pattern, "start middle"))  # Doesn't match

# 8. Greedy vs non-greedy matching
text = "<tag>content</tag><tag>more content</tag>"
greedy = re.findall(r"<tag>.*</tag>", text)
non_greedy = re.findall(r"<tag>.*?</tag>", text)
print(greedy)  # Output: ['<tag>content</tag><tag>more content</tag>']
print(non_greedy)  # Output: ['<tag>content</tag>', '<tag>more content</tag>']

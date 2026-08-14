# Day 15 - Strings in Python

text = "Artificial Intelligence"

print("Original:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())

# String indexing
print("First character:", text[0])
print("Last character:", text[-1])

# String slicing
print("First 10 characters:", text[:10])
print("Last 5 characters:", text[-5:])

# Replace
new_text = text.replace("Artificial", "Machine")
print("After replace:", new_text)

# Split
words = text.split()
print("Words:", words)

# Join
joined = "-".join(words)
print("Joined:", joined)

# Check substring
print("AI" in text)
print("Intelligence" in text)

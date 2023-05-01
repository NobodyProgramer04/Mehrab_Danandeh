import re

text = input()

# Remove any punctuation at the end of words
text = re.sub(r'[.,;:]+(\s|$)', ' ', text)

# Find all words that start with a capital letter
words = re.findall(r'\b[A-Z][a-z]*\b', text)

count = 0
for i in range(len(words)):
    count += 1
    print(f"{count}:{words[i]}")
        
if count == 0:
    print("None")
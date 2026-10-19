import re

text = "The brown bear"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
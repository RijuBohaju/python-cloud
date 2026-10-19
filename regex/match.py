import re

text = "The brown bear"
pattern = r"brown"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
import re

text = "The brown bear"
pattern = r"brown"

replacement = "black"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
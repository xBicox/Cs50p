#User in puts text.
text = input("")

#Text is stripped of spaces off the sides and then repalces spaces
# in the middle of the text with "...".
text = text.strip()
text = text.replace(" " , "..." )

# Prints replaced text.
print(f"{text}")

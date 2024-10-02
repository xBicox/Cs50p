camelCase = input("camelCase: ").strip()

for letter in camelCase:
    if letter.isupper():
        camelCase = camelCase.replace(letter, "_" + letter.lower())

print("snake_case:", camelCase)

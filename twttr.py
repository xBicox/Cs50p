vowels = ["a","e","i","o","u","A","E","I","O","U"]

message = input("Input: ").strip()

for vowel in vowels:
    message = message.replace(vowel, "")

print("output:", message)

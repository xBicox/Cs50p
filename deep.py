#Ask user question
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#Check if answer is correct
match answer.strip().casefold():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

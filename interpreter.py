expression = input("Expression:")

variable = expression.split(" ")

x = int(variable[0])
y = variable[1]
z = int(variable[2])

if y == "+":
    print(float(x+z))

elif y =="-":
    print(float(x-z))

elif y == "*":
    print(float(x*z))

elif y == "/":
    print(float(x/z))

calc_help = input("Do you need a symbol chart? (y/n): ").lower()

num = float(input("Enter a number: "))
symbol = input("Enter a symbol: ")
num2 = float(input("Enter another number: "))


if calc_help == "y":
    print("+, -, *, /, **(exponent), **.5(square root), %")

if symbol == "+":
    print(num + num2)
elif symbol == "-":
    print(num - num2)
elif symbol == "*":
    print(num * num2)
elif symbol == "/":
    print(num / num2)
elif symbol == "**":
    print(num ** num2)
elif symbol == "%":
    print(num % num2)
else:
    print("Please enter a valid symbol.")

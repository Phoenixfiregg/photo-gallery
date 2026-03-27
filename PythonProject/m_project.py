import random
hint = ["It is a number that little kids use to say the", "It is a number you can never reach if you count", "The number is not actually a number but a word", "It is the idea of something with no end", "You use a symbol that looks like an 8 but its rotated"]
secrets_number = "infinity"

while True:
    guess_number = input("Guess how much I love you: ").lower()
    if guess_number == secrets_number:
        print("You win")
        break

    print("Guess again. Want a hint?")
    hint_answer = input("Yes or No? ").lower
    if hint_answer() == "yes":
        print(random.choice(hint))

print("Will you be my valentines?")
while True:
    answer = input("Yes or No? ").lower()
    if answer in ["yes", "no"]:
        break
        print("Please type yes or no.")
if answer == "yes":
    print("Yayyy, I love you so much baby")
else:
    print("Did your other hoes already ask you out?")
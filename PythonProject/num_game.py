import random
rps_wins = 0
coin_wins = 0
tries = 0
answer = random.randint(1,100)
def coin_flip():
    global coin_wins
    while coin_wins < 3:
        coin_guess = input("Heads or Tails? ").lower()
        flip = random.choice(["heads", "tails"])
        if coin_guess == flip:
            print(f"Correct! It was {flip}")
            coin_wins += 1
        else:
            print(f"Wrong! It was {flip}")

def play_game():
    global rps_wins
    while rps_wins < 3:
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            rps_wins += 1
        else:
            print("Computer wins!")
    coin_flip()


while tries < 6:
        guess = int(input("Guess the number (1-100): "))
        if guess > answer:
            print("Too high")
            tries += 1
        elif guess < answer:
            print("Too low")
            tries += 1
        else:
            print("Correct")
            play_game()
            break

print(f"The answer was: {answer}")



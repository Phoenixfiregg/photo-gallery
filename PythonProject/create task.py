
def pi_game(correct_answer):
    tries = 10
    digit_count = len(str(correct_answer).replace(".", ""))
    guesses = []
    print(f"Your goal is to get the first {digit_count} digits of pi to win!")

    while tries > 0:
        pi_digit = input(f"\nEnter the first {digit_count} digits of pi: ")
        if pi_digit in guesses:
            print("\nYou have already guessed that!")
            continue
        guesses.append(pi_digit)
        tries -= 1
        if pi_digit == correct_answer:
            print("\nYou win!")
            print("Your guesses were:", guesses)
            return

        print("\nWrong! Try again.")
        print(f"\nYou have {tries} tries left!")

        if tries == 8:
            hint = input("\nDo you want to help? (y/n): ").lower()
            if hint == "y":
                print("The first 2 digits of pi is 3.1")
        if tries == 6:
            hint = input("\nDo you want to help? (y/n): ").lower()
            if hint == "y" and digit_count > 4:
                print("The first 4 digits of pi is 3.141")
            elif digit_count <= 4:
                print("\nYour difficulty too easy for another hint!")
            elif hint == "n":
                print("\nYou might have needed that hint.")

    print("Your guesses were:", guesses)
    print("You lose!")

difficulty = input("Choose your difficulty(easy, normal, hard): ").lower()
if difficulty == "easy":
    pi_game("3.141")
elif difficulty == "normal":
    pi_game("3.1415")
elif difficulty == "hard":
    pi_game("3.141592")
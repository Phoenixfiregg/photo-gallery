import time
def escape_room():
    print("You wake up in a locked room.")
    print("\nIf you need help, type 'help'.")
    moves_left = 12
    math_solved = False
    has_key = False
    key_taken = False
    code = 351
    current_location = "center"
    while True:
        print(f"\nMoves left: {moves_left}\n")
        commands = input("What do you do? ").lower()
        if commands == "left":
            print("You see a door")
            moves_left -= 1
            current_location = "left"


        elif commands == "use key" and current_location == "left":
            moves_left -= 1
            if has_key:
                print("You unlocked the door and escaped!")
                time.sleep(1)
                print("\nWait there's another door...")
                print("It is a 3 digit code")
                guess = int(input("\nGuess the code: "))
                moves_left -= 1
                if guess == code:
                    print("\nYou unlocked the door and escaped! 🎉")
                    break
                else:
                    print("Wrong code. Try again later.")
            else:
                print("You need a key")




        elif commands == "right":
            print("You see a table")
            moves_left -= 1
            current_location = "right"


        elif commands == "look":
            if math_solved and not key_taken:
                print("You see a key on the table.")
            elif not math_solved:
                print("There is nothing useful here.")
            else:
                print("The table is empty.")
            moves_left -= 1


        elif commands == "pick up":
            if math_solved and not key_taken:
                print("You picked up the key.")
                has_key = True
                key_taken = True
                moves_left -= 1
            elif not math_solved:
                print("There is no key to pick up yet.")
                moves_left -= 1
            else:
                print("You already have the key.")
            moves_left -= 1



        elif commands == "up":
            print("There is a math problem")
            answer = input("What is (3*10)+100? ")
            moves_left -= 1
            current_location = "up"
            if answer == "130":
                print("Correct! A key appears on the table.")
                math_solved = True
            else:
                print("Wrong answer. Try again later.")
                moves_left -= 1



        elif commands == "down":
            current_location = "down"
            print("You see a sticky note")
            time.sleep(1)
            print("\nIt says 3 yellow dogs, 5 orange fish, and 1 white cat.")
            moves_left -= 1


        elif commands == "help":
            print("\nCommands: left, right,up, down,")
            hints = input("\n Would you like to pay for more hints for 1 move? (y/n) ").lower()
            if hints == "y":
                print("\nlook, use _____, pick up")
                moves_left -= 1


        elif commands == "use key" and not current_location == "left":
            print("You can't use the key here")
            moves_left -= 1


        if moves_left == 0:
            print("\nYou ran out of moves. Game over 💀")
            break



escape_room()
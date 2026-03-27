import json
from datetime import datetime, timedelta

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"games": [], "money": [], "school": []}
def save_data(data):
    with open("data.json", "w") as f:
         json.dump(data, f)

def add_game(data):
    name = input("Game name: ")
    status = input("Status (playing/backlog/finished): ")
    game = {"name": name, "status": status}
    data["games"].append(game)
    save_data(data)
    print("Game added")

def add_expense(data):
    description = input("What you spent money on: ")
    amount = float(input("How much did it cost: ").replace("$", ""))
    expense = {"description": description, "amount": amount}
    data["money"].append(expense)
    save_data(data)
    print("Expense added")

def add_assignment(data):
    name = input("name: ")
    due_data = input("due: ")
    assignment = {"name": name, "due": due_data}
    data["school"].append(assignment)
    save_data(data)
    print("Assignment added")

def delete_assignment(data):
    if not data["school"]:
        print("No assignments to delete!")
        return
    for i, assignment in enumerate(data["school"]):
        print(f"   {i+1}.", assignment["name"], "-", assignment["due"])
    assignment_number = int(input("Which number to delete? "))
    data["school"].pop(assignment_number - 1)
    save_data(data)
    print("Assignment deleted!")

def delete_game(data):
    if not data["games"]:
        print("No games to delete!")
        return
    for i, game in enumerate(data["games"]):
        print(f"   {i+1}.", game["name"], "-", game["status"])
    game_number = int(input("Which number to delete? "))
    data["games"].pop(game_number - 1)
    save_data(data)
    print("Game deleted!")

def delete_expense(data):
    if not data["money"]:
        print("No expenses to delete!")
        return
    for i, expense in enumerate(data["money"]):
        print(f"   {i + 1}.", expense["description"], "-", f"${expense['amount']:.2f}")
    expense_number = int(input("Which number to delete? "))
    data["money"].pop(expense_number - 1)
    save_data(data)
    print("Expense deleted!")

def main():
    data = load_data()
    action = input("What do you want to do? (view/add game/add expense/add assignment/delete assignment/delete game/delete expense): ")
    if action == "add game":
        add_game(data)
    elif action == "add expense":
        add_expense(data)
    elif action == "add assignment":
        add_assignment(data)
    elif action == "delete assignment":
        delete_assignment(data)
    elif action == "delete game":
        delete_game(data)

    elif action == "delete expense":
        delete_expense(data)
    print("""
        =====================================
                MY DAILY DASHBOARD
        =====================================

        🎮 GAMES
        -------------------------------------""")

    for game in data["games"]:
        print("   ", game["name"], "-", game["status"])
    if not data["games"]:
        print(" (no games yet)")

    print("""
        💰 MONEY
        -------------------------------------
        """)
    for expense in data["money"]:
        print("   ", expense["description"], "-", f"${expense['amount']:.2f}")
    if not data["money"]:
        print("    (no expenses yet)")
    total = sum(expense["amount"] for expense in data["money"])
    print(f"    Total spent: ${total:.2f}")
    print("""📚 SCHOOL
        -------------------------------------""")
    today = datetime.today()
    data["school"].sort(key=lambda x: x["due"])
    for assignment in data["school"]:
        due_date = datetime.strptime(assignment["due"], "%Y-%m-%d")
        if due_date - today <= timedelta(days=2):
            print("   ⚠️", assignment["name"], "- DUE SOON:", assignment["due"])
        else:
            print("   ", assignment["name"], "-", assignment["due"])
    if not data["school"]:
        print("    (no assignments yet)")


main()
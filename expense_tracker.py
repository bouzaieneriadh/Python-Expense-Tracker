expenses = []

def add_expense():
    description = input("Description: ")
    amount = float(input("Amount: "))
    expenses.append({"description": description,"amount": amount})
    print("Expense added <3 <3!")


def show_expenses():
    if len(expenses)==0:
        print("No expenses recorded.")
    else :
        n=1
        for expense in expenses :
            print(f"{n}.{expense['description']}-{expense['amount']:.2f}")
            n+=1

def show_total():
    total = 0
    for expense in expenses :
        total+=expense["amount"]
    print(f"Total: {total:.2f}")

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1.Add an expense")
        print("2.View expenses")
        print("3.Show total")
        print("4.Exit")
        choice = input("Your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()

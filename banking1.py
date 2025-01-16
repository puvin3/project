# Initializing account details
holder_name = input("Enter your name: ")
balance = 0
while True:
    print("\n----- Bank System Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Please choose an option: ")
    if choice == "1":
        print(f"Current balance: {balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited {amount}. Current balance: {balance}")
        else:
            print("Invalid amount. Please enter a positive number.")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"Withdrew {amount}. Current balance: {balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive number.")
    elif choice == "4":
        print("Thank you for using the banking system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

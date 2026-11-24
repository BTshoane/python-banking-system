# Load balance from file 
try:
    with open("balance.txt", "r") as file:
        balance = float(file.read())
except:
    balance = 0 

while True:
    print("\n== BANKING SYSTEM ===")
    print("1. Check Balance") 
    print("2. Deposit Money") 
    print("3. Withdraw Money") 
    print("4. Exit")  

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your Balance is: R{balance}")

    elif choice == "2":
        amount_input = input("Enter amount to deposit: ")

        try:
            amount = float(amount_input) 

            if amount > 0:
                balance += amount

                with open("balance.txt", "w") as file:
                    file.write(str(balance)) 

                print(f"Deposited: R{amount}")
            else: 
                print("Enter a valid amount.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == "3": 
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount > 0:
                if amount <= balance:
                    balance -= amount

                    # Save balance
                    with open("balance.txt", "w") as file:
                        file.write(str(balance))

                    print(f"Withdrawn: R{amount}")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid input.")

        except ValueError:
            print("Invalid input.")

    elif choice == "4":
        print("Goodbye 👋🏼")
        break

    else:
        print("Invalid option.")        


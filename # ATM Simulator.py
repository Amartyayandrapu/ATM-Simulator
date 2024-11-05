# ATM Simulator

bal = 1000 
transactions = []

while True:
    print("\nChoose a process:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Mini Statement")
    print("5. Exit")

    op = input("Enter your option: ")

    if op == '1':
        print(f"The balance is: ${bal}")

    elif op == '2':
        amt = float(input("Enter amount to deposit: "))
        if amt <= 0:
            print("Incorrect deposit amount")
            continue
        bal += amt
        transactions.append(f"Deposited: ${amt}")
        print(f"${amt} deposit successful")

    elif op == '3':
        amt = float(input("Enter amount to withdraw: "))
        if amt <= 0:
            print("Incorrect withdrawal amount")
            continue
        if amt > bal:
            print("Insufficient balance")
        else:
            bal -= amt
            transactions.append(f"Withdraw: ${amt}")
            print(f"${amt} withdrawal successful")

    elif op == '4':
        if transactions:
            print("Mini Statement:")
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions found")

    elif op == '5':
        print("Exited")
        break

    else:
        print("Invalid option!")

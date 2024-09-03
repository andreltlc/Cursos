menu = """

[1] Deposit
[2] Balance
[3] Extract
[4] Quit

"""

balance = 1000
limit = 500
extract = ""
withdrawals = 0
LIMIT = 3

while True:

    option = input(menu)

    if option == "1":
        value = float(input("Enter the deposit amount: "))

        if value > 0:
            balance += value
            extract += f"deposits: R$ {value:.2f}\n"

        else:
            print("Operation failed! The value entered is invalid.")

    elif option == "2":
        value = float(input("Enter the withdrawals value: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdrawals = withdrawals >= LIMIT

        if exceeded_balance:
            print("Operation failed! You do not have enough balance.")

        elif exceeded_limit:
            print("Operation failed! Withdrawals amount exceeds limit.")

        elif exceeded_withdrawals:
            print("Operation failed! Maximum number of withdrawals exceeded.")

        elif value > 0:
            balance -= value
            extract += f"withdrawals: R$ {value:.2f}\n"
            withdrawals += 1

        else:
            print("Operation failed! The value entered is invalid.")

    elif option == "3":
        print("\n================ extract ================")
        print("No financial transactions were made." if not extract else extract)
        print(f"\nbalance: R$ {balance:.2f}")
        print("==========================================")

    elif option == "4":
        break

    else:
        print("Invalid operation, please select the desired operation again.")
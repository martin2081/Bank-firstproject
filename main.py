import getpass


def create_username():
    while True:
        create_username.username = input("Create a username at least 6 characters long: ")
        if len(create_username.username) >= 6:
            new_username = create_username.username
            break
        else:
            print("ERROR username must be more than 6 characters ")
    return new_username


def create_password():
    while True:
        password = getpass.getpass("Create at least a 4 digit password: ")
        if password.isdigit():
            if len(password) >= 4:
                i = 0
                while i < 3:
                    temporary_password = getpass.getpass("Verify password: ")
                    if temporary_password == password:
                        return password
                    else:
                        i += 1
                        print("Wrong password.")
                else:
                    print("To many attempts account has been lock.")
                    break
            else:
                print("Password must be at least 4 digits")
        else:
            print("Password must be digits")


def deposit():
    while True:
        amount = input("Enter amount of deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a number")
    return amount


def withdraw(balance):
    while True:
        withdraw_amount = input("How much do you want to withdraw?: ")
        if withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
            if withdraw_amount > balance:
                print("Your dont have enough to withdraw that amount. \n"
                      f"Current Balance: {balance} \n")
            else:
                balance -= withdraw_amount
                break
        else:
            print("Enter a valid number")


def main():
    balance = 0
    create_username()
    create_password()
    while True:
        answer = input("Press 1 to deposit: \n"
                       "Press 2 to withdraw: \n"
                       "Press 3 to check balance: \n"
                       "Press 4 q to quit: \n")
        if answer == "1":

            balance = deposit()
        elif answer == "2":
            withdraw(balance)
        elif answer == "3":
            print(f"Balance: ${balance}")
        elif answer == "q":
            break
        else:
            print("Invalid command")


main()
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, "r") as file:
            self.balance = int(file.read())

    def reload_balance(self):
        with open(self.filepath, "r") as file:
            self.balance = int(file.read())

    def view_balance(self):
        self.reload_balance()
        return self.balance

    def withdraw(self, amount):
        self.reload_balance()
        with open(self.filepath, "w") as file:
            file.write(str(self.balance - amount))

    def deposit(self, amount):
        self.reload_balance()
        with open(self.filepath, "w") as file:
            file.write(str(self.balance + amount))


account = Account("balance.txt")
flag = True
while flag:
    given = input("What would you like to do? V (View Balance), W (Withdraw), or D (Deposit)? ").lower()
    if given == "v":
        print(account.view_balance())
    elif given == "w":
        account.withdraw(int(input("How much would you like to withdraw? ")))
        print(f"{account.view_balance()} dollars remaining")
    elif given == "d":
        account.deposit(int(input("How much would you like to deposit? ")))
        print(f"{account.view_balance()} dollars remaining")
    else:
        print("Sorry, I cannot understand you.")

    flag_conditional = input("Would you like to do something else? Y/N ").lower()
    if flag_conditional == "y":
        continue
    elif flag_conditional == "n":
        break
    else:
        print("Sorry, I cannot understand you.")
        break

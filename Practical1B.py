class Bank:
    def __inf__ (self):
        self.balance = 0
        print("7_GovindSaini \n")
        print("The account is created.")
        
    def deposit(self):
        amount = float(input("Enter the amount to be deposit:"))
        self.balance = self.balance + amount
        print("The deposit is successful and the balance of the acount is %f" % self.balance)
    
    def withdraw(self):
        amount = float(input("Enter the amount to be Withdraw:"))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("The withdraw is successful and the balance of the acount is %f" % self.balance)
        else:
            print("Insufficient balance")
    
    def enquiry(self):
        print("Balance in the account is %f" % self.balance)
        
acc = Bank()
acc.deposit()
acc.withdraw()
acc.enquiry()        
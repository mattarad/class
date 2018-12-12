class bankAccount():
    
    """This is a Noraml Account type"""
    
    accountType = 'Normal Account'
    members = 0

    
    def __init__(self,name,birth,balance):
        self.name = name
        self.birthDate = birth
        self.balance = balance
        bankAccount.members += 1
        print("ACCOUNT CREATED")
        print('Welcome %s!'%(self.name))
        print('We are happy to add you to our family of %s strong!'%(bankAccount.members))
        
    def Deposit(self,amount):
        self.balance += amount
        see_balance = input('would you like to see your balance? Y/N:')
        if see_balance.lower() == 'y':
            return self.balance
        else:
            print('have a nice day :)')
    def Withdraw(self,amount):
        if amount <= self.balance:
            if amount >= 7500:
                print('$7500 on a Saint Laurent Jacket\nyeah.')
            self.balance -= amount
            see_balance = input('would you like to see your balance? Y/N:')
            if see_balance.lower() == 'y':
                return self.balance
            else:
                print('have a nice day :)')
                
        else:
            print('insufficient funds')

            
    def Balance(self):
        if self.balance > 999999:
            print('I got 1-2-3-4-5-6-7-8\nMs in my Bank Account\nYeah')
        else:
            print("your balance is: %s"%(self.balance))
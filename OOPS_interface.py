class ATM:
    #creating a constructor that will call menuy
    def __init__(self):
        self.pin=0
        self.balance=0
        while True:
            self.menu()   #calling menu function

    def menu(self):
        print("""
                            Welcome to the J&K bank
                            1. Enter 1 For Creating New Pin
                            2. Enter 2 For Depositing Money
                            3. Enter 3 For Withdrawl
                            4. Enter 4 To Check Balance
                            5. Enter 5 To Exit
                         """)
        try:
            choice=int(input("Enter Your Choice:: "))
            if choice==1:
                self.create_pin() #self i.e. reference to object is passed by default
            elif choice==2:       # because in OOps only object can access method or data
                self.deposit_money()
            elif choice==3:
                self.withdraw_money()
        except Exception as e:
            print("Choice should contain integers only!")

    def create_pin(self):
        try:
            old_pin=int(input("Please Enter Your OLD Pin::"))
            if self.pin == old_pin:
                try:
                    new_pin=int(input("Enter Your New Pin::"))
                    self.pin=new_pin
                    print("Your Pin is Created Successfully!")
                except Exception as e:
                    print(f"An Exception has Occured in your new Pin {e}")
            else:
                print("The Entered Pin is Incorrect!")
        except Exception as e:
            print(f"Got an Exception{e}")
            
    
    def deposit_money(self):
        try:
            temp_pin=int(input("Enter Your PIN::"))
            if temp_pin==self.pin:
                try:
                    amount=int(input("Enter The Amount You Want to Deposit::"))
                    self.balance+=amount
                    print("Your Amount has been deposited Successfully!")
                except Exception as e:
                    print("Amount Should Contain Integers Only!")
            else:
                print("Wrong Pin entered!")
        except Exception as e:
            print("The PIN Accepts Only Integers as Input")

    def withdraw_money(self):
        try:
            temp_pin=int(input("Enter Your PIN::"))
            if temp_pin==self.pin:
                try:
                    amount=int(input("Enter The Amount You Want to withdraw::"))
                    if amount<=self.balance:
                        self.balance-=amount
                        print("Your Amount has been Withdrawed Successfully!")
                    else:
                        print("Insufficient Amount in the Bank!")
                except Exception as e:
                    print("Amount Should Contain Integers Only!")
            else:
                print("Wrong Pin Entered!")
        except Exception as e:
            print("The PIN Accepts Only Integers as Input")


sbi=ATM()
            
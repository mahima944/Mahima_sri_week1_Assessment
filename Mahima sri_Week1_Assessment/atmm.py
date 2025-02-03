def check_balance(balance):
    print(f"The balance in the account is: {balance}")
    
def check_deposite(balance):
    amount=float(input("enter the amount: "))
    if amount>0:
        balance+=amount
        print(balance)
    else:
        print("invalid deposite")
    return balance 

def check_withdraw(balance):
    amount=float(input("enter the amount: "))
    if amount<=balance:
        balance-=amount
        print(balance)
    else:
        print("insufficient")
    return balance

def main():
    
    balance=1000.00
    while(True):
        choice= input("enter your choice(1-4):")
        if choice=='1':
            check_balance(balance)
        elif choice=='2':
            balance=check_deposite(balance)
        elif choice=='3':
            balance=check_withdraw(balance)
        elif choice=='4':
            print("exit")
            break
        else:
            print("invalid")
main()
        
    
        
        
        
       
account_holder=None
balance=0
while True:

    print('\nBanking System Menu:')

    print('1. Create account')
    print('2.View Account')
    print('3.Deposit')
    print('4.withdraw')
    print('5.Check Balance')
    print('6.exit')
    choice = input('enter your choice:')
    if choice == '1':
        account_number=input('enter account number:')
        account_holder=input('enter account holder name:')
        initial_balance=float(input('enter initial balance:'))
        if initial_balance >=0:
            balance=initial_balance
            print(f'Account created successfully! Welcome,{account_holder}.Your balance is {initial_balance}')
        else:
            print('account number already exists.')
    elif choice=='2':

        if account_holder:
            print(f"Account Holder: {account_holder}")
            print(f"Current Balance: {balance}")
        else:
            print('account not fount')
    elif choice=='3':
        if account_holder:
            Amount =float(input('enter amount to deposit:'))
            if Amount>0:
                balance+=Amount
                print(f'Deposited{Amount}.current balance{balance}')
            else:
                print('invalid amount.please enter a positive number')
        else:
            print('account not found')
    elif choice=='4':

        if  account_holder:
            amount=float(input('enter amount to withdraw:'))
            if amount>0:
                if amount<=balance:
                    balance-=amount
                    print(f'withdrew{amount}.current balance{balance}')
                else:
                    print('insufficient funds.')

            else:
                print('you need to open an account first.')

            
        else:
            print('account not found')
    elif choice=='5':

        if account_holder:

            print(f'account balance:{balance}')
        else:
            print('account not fount')
    elif choice=='6':
        print('exiting the program.')
        breakpoint()
    else:
        print('invalid choice.please try again.')

    

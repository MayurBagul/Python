print("We are Selling House At Price 1 Million Dollers !")
willing=input("Do you willing to buy this House (yes/no) ? :- ")

if willing=='yes':
    credit=int(input("Enter Your Credit it must be greater than 1 Million Dollers "))

    if credit>1000000:
        print("Hello Sir \n \n Your are Eligible to buy this house by putting down 10% ammount .")
        down_payment=10/100*1000000
        print(f'You Have to do {down_payment} Down Payment on specified House Price')
    else:
        print("I'm Sorry Your credit score is fail to eligible for doing less down payment.\n But you can buy this house by putting down 20% of whole ammount")
        down_payment=20/100*1000000
        print(f'You Have to do {down_payment} Down Payment on specified House Price')


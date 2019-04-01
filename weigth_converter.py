print("Welcome To Weight Converter !")

weight=int(input("Enter Your Weight :- "))
converter=input("In Pounds(L) / In Kg(K):")

if converter=='l' or 'L':
    kg=weight*0.454
    print(f' Weight is = {kg} kg')
elif converter=='k' or 'K':
    pnd=weight/0.454
    print(f' Weight is = {pnd} lbs ')
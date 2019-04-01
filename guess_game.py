secret_number=9

guess_count=0
guess_limit=3

guess=0

while guess_count<guess_limit:
    guess=int((input("Guess the number := ")))
    guess_count+=1
    if guess==secret_number:
        print("Here You win the Game !")
        break

else:
    print("Sorry You Have lots all the changes !")







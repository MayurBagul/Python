print("Welcome To car Game ! \n Type Help to Know More about how to play this game !\n")

command=''

while command!=quit:
    command=input("> ").lower()
    if command == 'start':
        print("Car is Started !")
    elif command == 'stop':
        print("Car is Stopped !")
    elif command == 'help':
        print("""   
        Start - Start the Game !
        Stop - To Stop the Game !
        Quite - To Exit the Game""")
    elif command == 'quit':
        print("You are Exited the game !")
        break
    else:
        print("You Have Entered Wrong Choice !")




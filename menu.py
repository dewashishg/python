import sys
def mainMenu():
    print("1. Do something good")
    print("2. Do something bad")
    print("3. Quit")
    while True:
        try:

            choice = int(input("Select your choice: "))
            if choice == 1:
                good()
                break
            elif choice == 2:
                bad()
                break
            elif choice == 3:
                break
            else:
                print("select choice between 1-3")
                mainMenu()
        except ValueError:
            print("Invalid selection of choice, select between 1-3")
    sys.exit()
def good():
    print("Thanks for choosing Good")

def bad():
    print("You have selected Bad menu")
mainMenu()

import sys
def keep_going():


    while True:
        try:
            playing = input("Do you want to play quiz? ").lower()
            score = 0
            if playing == "yes":
                print("Okay, thats great then lets start")
                q1 = input("what is cpu? ")
                if q1 == 'central processing unit':
                    print("correct")
                    score += 1
                else:
                    print("incorrect")
                q2 = input("what is gpu? ")
                if q2 == 'graphic processor unit ':
                    print("correct")
                    score += 1 
                else:
                    print("incorrect")
                print("you have scored " + str(score) + "marks in the quiz")
                print(" you have scored " + str((score/2)*100) + "%")
                break

            else:
                print("You have chosen to quit this program")
                break
        except ValueError:
            print("You have entered incorrect keyword, pls enter text only")
    sys.exit()
keep_going()
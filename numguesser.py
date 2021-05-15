import random

random.seed()


def checkNum(usernum, message):
    while True:
        try:
                usernum = int(input(message))
        except ValueError:
                print("Thats not an integer! Please try again.")
                continue
        else:
                if (usernum < 0):
                    print("Thats an invalid integer. Please try again.")
                    continue
                else:
                    break
                break
    return usernum


def main ():
    lownum = 0
    highnum = 0
    score = 0
    print("Welcome to the number guesser!")
    name = str(input("Tell us your name: "))
    print("Well hello there, ", name, ", we're happy to have you!")
    print("Here, you'll guess between two numbers.")

    lownum = checkNum(lownum, "Please enter your low, non-negative integer: ")
    highnum = checkNum(highnum, "Please enter your high, non-negative integer: ")
    score = checkNum(score,"Please enter your starting score: ")

    while True:
        if (highnum < lownum):
            print("Your high number is lower than your low number! Please try again.")
            highnum = checkNum(highnum, "Please enter your high, non-negative integer: ")
        else:
            break

    while True:
        if (score <= 0):
            print("No more points! Come back again.")
            break
        randomnumber = random.randint(lownum,highnum)
        scoreReduction = score % 10
        while True:
            try:
                userguess = int(input("Please enter your guess: "))
                if (userguess > randomnumber):
                    print("Too high! Try again.")
                    score = score - scoreReduction
                elif (userguess < randomnumber):
                    print("Too low! Try again.")
                    score = score - scoreReduction
                else:
                    print("You got it!")
                    break
            except ValueError:
                print("Invalid input.")
        print("Loop exited.")
        print("Your score is: " + str(score))
        # while True:
        #     goAgain = str(input("Would you like to play again? Enter a y or n: "))
        #         if(goAgain.lower == "y"):
        #             continue
        #         elif(goAgain.lower == "n"):
        #             print("Thanks for playing!")
        #             break
        #         else("")
        
        # finally:
        #     continue

        
        
        
        



if __name__ == "__main__":
    main()

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

    # while True:
    #     if (score <= 0):
    #         print("No more points! Come back again.")
    #         break
    #     randomnumber = random.randint(lownum,highnum)

        
        



if __name__ == "__main__":
    main()
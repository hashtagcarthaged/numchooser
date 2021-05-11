import random

random.seed()

def checkNum(usernum, numtype):
    while True:
        try:
                usernum = int(input("Please enter your " + numtype + " non-negative number: "))
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

    lownum = checkNum(lownum, "low")
    highnum = checkNum(highnum, "high")

        



if __name__ == "__main__":
    main()
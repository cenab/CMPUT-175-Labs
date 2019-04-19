from random import *
def main():
    randomnumber = randint(1, 100)
    print("Game Session Starts")
    print("Enter coins values as 1-penny, 5-nickel, 10-dime, and 25-quarter.")
    print("Enter coins that add up to", randomnumber, "cents, one per line.")
    list = []
    coins = [1, 5, 10, 25]
    t = True
    while t == True:
        n = input("Enter a valid coin value >")
        if n.isdigit() == True:
            n = int(n)
        if n in coins:
            t = True
            list.append(int(n))
        if n not in coins and n != "":
            print("Invalid entry - Try again!")
            t = True
        if n == "":
            t = False
            print("Session Ends!")
            print("Game Session Ends")
            print("Here is the outcome :")
            print("Failure - you only entered", sum(list), "cents")
            print("You are short of",randomnumber - sum(list), "cents")
            gameover = input("Play another game session (y/n)?")
            if gameover == "y":
                main()
            if gameover == "n":
                print("Thanks for playing ... goodbye")
        if sum(list) == randomnumber:
            t = False
            print("Game Session Ends")
            print("Here is the outcome :")
            print("Success!")
            gameover = input("Play another game session (y/n)?")
            if gameover == "y":
                main()
            if gameover == "n":
                print("Thanks for playing ... goodbye")
        if sum(list) > randomnumber:
            t = False
            print("Game Session Ends")
            print("Here is the outcome :")
            print("Failure - you entered", sum(list),  "cents")
            print("The amount exceeds", randomnumber, "cents by", sum(list)-randomnumber, "cents")
            gameover = input("Play another game session (y/n)?")
            if gameover == "y":
                main()
            if gameover == "n":
                print("Thanks for playing ... goodbye")
    return

if __name__ == '__main__':
    main()

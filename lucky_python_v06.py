#Random
import random

# This is a reusable piece of code that the programmer can re-use whenever their is a yes/no question.

def yes_no(question,yes, no, error):
    
    # Lists Used in Yes_No Checker    
    yes_answers = ["y","yes"]
    no_answers = ["n", "no"]
    valid_answers = ["n", "no","y","yes"]
    
    valid = False
    while not valid:

        response = input (question).lower()

        if response not in valid_answers:
            print(error)
        elif response in yes_answers:
            print(yes)
            return response
        elif response in no_answers:
            print(no)
            return response

# This is a number checker so we dont get unwanted errors during the code
def num_check(question, error):

    valid = False
    while not valid:
         try:
             response = int(input(question))
             if 0 < response <= 10:
                return response
             else:
                print(error)
         except ValueError:
             print(error)
 
# This is a function that Calculates which  reward you get 
def game_calc():
    valid = False

    while not valid:
        input("1. 2. 3...\n")
        choosen_num = random.randint(1,100000)
        if choosen_num <= 100:
            return 5
        elif choosen_num <= 1000:
            return 0.5
        elif choosen_num <= 10000:
            return 0.1
        else:
            return 0
    


#Statement Gen
def statement_gen(statement, decoration) :
    sides = decoration * 3
    statement = ("{} {} {}".format(sides,statement,sides))
    topbottomlenth = len(statement) - 9 # Number cannot * a string in the same variable
    topbottomv2 = topbottomlenth * decoration 

    print(topbottomv2)
    print(statement)
    print(topbottomv2)

    return ""

# ***** Main Routine goes here *****
    
# Yes No
played_before = yes_no("Have you played before? ","All Right Sweet","Here are the instructions\n\nYou enter money (No less then 1$ no more then 10)\nRounds cost 1$. Every round you could win\na Unicorn","That is not a valid answer")
print("\nOk Lets get started")

# Input Money 
payment = num_check("How much would you like to play with? ","Please Enter a whole number between 1 and 10\n" )

print("You have spent ${}\n".format(payment))

game_begins = statement_gen("\x1B[32mGame Begins\x1B[0m","^")
rounds_played = 0
# This is The program that runs the function that makes you run out of money.
while payment > 0.99:
    games = game_calc()
  # This is all the names of things set to a color so they come out in a different color.
    if games == 5:
        outcome = "\x1B[34mUnicorn!\x1B[0m"
    elif games == 0.5:
        outcome = "\x1B[36mZebra!\x1B[0m"
    elif games == 0.1:
        outcome = "\x1B[32mDonkey!\x1B[0m"
    else:
        outcome = "\x1B[95mTroll!\x1B[0m"

    

    rounds_played += 1
    payment = payment - 1 + games

    print("You got a {}\n".format(outcome))
    print( "Your balance is ${:.2f}".format(payment))

    input("Press enter to continue...\n")

game_ends = statement_gen("\x1B[34mGame Ends\x1B[0m","^")


    






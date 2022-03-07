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
        print("\n")
        choosen_num = random.randint(1,100000)
        if choosen_num <= 200:
            return 5
        elif choosen_num <= 10000:
            return 0.5
        elif choosen_num <= 20000:
            return 0.1
        else:
            return 0
    


#Statement Gen
def statement_gen(statement, decoration,lines) :
    sides = decoration * 5
    statement = ("{} {} {}".format(sides,statement,sides))
    if lines == 3:
        
        
        topbottomlenth = len(statement) - 9 # Number cannot * a string in the same variable
        topbottomv2 = topbottomlenth * decoration 

        print(topbottomv2)
        print(statement)
        print(topbottomv2)

        
    else:
        print(statement)
    
    return ""
        
        



# ***** Main Routine goes here *****
    
# Yes No
played_before = yes_no("Have you played before? ","All Right Sweet","Here are the instructions\n\nYou enter money (No less then 1$ no more then 10)\nRounds cost 1$. Every round you could win\na Unicorn","That is not a valid answer")
print("\nOk Lets get started")

# Input Money 
payment = num_check("How much would you like to play with? ","Please Enter a whole number between 1 and 10\n" )

print("You have spent ${}\n".format(payment))

game_begins = statement_gen("\x1B[32mGame Begins\x1B[0m","^",3)
rounds_played = 0
# This is The program that runs the function that makes you run out of money.
repeat = ""
while payment > 1 and not repeat== "xxx":
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

    you_got = statement_gen(" You got a {}".format(outcome),"^","1")
    print( "  Your balance is \x1B[33m${:.2f}\x1B[0m".format(payment))

    repeat = input("  Press \x1B[1m<Enter>\x1B[0m to continue or type \x1B[1m<xxx>\x1B[0m to quit\n  ")
    
    



game_ends = statement_gen("\x1B[31mGame Ends\x1B[0m","^",3)


    






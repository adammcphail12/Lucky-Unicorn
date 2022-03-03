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
             if 0 < response <= 100:
                return response
             else:
                print(error)
         except ValueError:
             print(error)
 
# This is a function that Calculates which  reward you get 
def game_calc():
    donkey = "ehhheee  orrrrrr\nThats a donkey\n50 cents for ya johnny boy"
    unicorn = "You lucky thing! You got a unicorn\nThats 5$ bucks for you..."
    horse = "well i guess, after ur sell ur car\nYoull have a horse to ride home\non. Dont know how yall will\npay for it tho\nYou made 1 cent"
    troll = "well that sucked didnt it. \nYou got a troll"
    valid = False

    profit = 0

    while not valid:
        print("Allright\n\nAre Ya Readyy\nCause here we go....")
        choosen_num = random.randint(1,100000)
        if choosen_num <= 100:
            return 5
        elif choosen_num <= 1000:
            return 0.5
        elif choosen_num <= 10000:
            return 0.1
        else:
            return 0
    

# ***** Main Routine goes here *****
    
# Yes No
played_before = yes_no("Have you played before? ","All Right Sweet","Here are they instructions\n---Instructions TBC---","That is not a valid answer")
print("\nOk Lets get started")

# Input Money 
payment = num_check("How much would you like to play with? ","Please Enter a whole number between 1 and 10\n" )
print("You have spent ${}".format(payment))

print("\n\n------ Game Begins ------\n\n")
rounds_played = 0
# This is The program that runs the function that makes you run out of money.
while payment > 0.99:
    games = game_calc()

    if games == 5:
        outcome = "unicorn"
    elif games == 0.5:
        outcome = "zebra"
    elif games == 0.1:
        outcome = "donkey"
    else:
        outcome = "troll"

    

    rounds_played += 1
    payment = payment - 1 + games

    print("you got a {}.  Your balance is ${:.2f}".format(outcome, payment))

    input("Press enter to continue...\n\n")

print("Your balance is ${} today. \nHave a good day champ!".format(payment))


    






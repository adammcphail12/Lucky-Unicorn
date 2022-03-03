# Intro sequence
print("Hello, Welcome to my Game.")

#sets input and checks if its valid
Input = input("Type in your answer below and then press enter\n(Acceptable answers include y, yes, no, n) \nHave you played before? ")

valid_answers = ["yes", "y","YES", "Yes", "no", "n", "NO","No",]

    
while Input not in valid_answers:
    print("Your answer was not valid \nPlease try again")
    Input = input("Type in your answer below and then press enter\n(Acceptable answers include y, yes, no, n): ")

#Variables
noAnswers = ["no", "n" "No" "NO"]
yesAnswers = ["yes", "Yes", "y", "YES"]
noTrue = "false"

#Rules
if Input in noAnswers:
    noTrue = "true"
    while noTrue == "true":
     input("Rules TBC  \n(Press Enter When Ready)")
     Input = input("Would you like to read again?: ")
     if Input not in valid_answers:
         print("Your answer was not valid \nPlease try again")
         Input = input("Type in your answer below and then press enter\n(Acceptable answers include y, yes, no, n): ")
     if Input in noAnswers:
         noTrue = "false"


print("\nCoolio, Lets Get Started...\n(Press Enter to continue)")
input("")

# After this we start up the actual game
# This Program Confirms The Amount of moeny a user wants to input. Throws a error nmessage when wrong.
confirm = "false"
cashConfirm = "false"
while cashConfirm == "false":
    inputMoney = int(input("How much money would you like to input?\n(No more then 10$): "))
    while inputMoney > 10:
        print("Sorry that is to much money\nYou are only allowed to spend ten")
        input("")
        inputMoney = int(input("How much money would you like to input?\n(No more then 10$): "))

    print("\nOk cool. \n You have spent {} ".format(inputMoney,))
    Input = input("Confirm?")
    if Input in yesAnswers:
       print("Ok, Lets get started")
       cashConfirm = "true"
    elif Input in noAnswers:
       print("Ok Cool. Lets Try That again.\nPress Enter")
       input("")
    else:
       while Input not in valid_answers:
           print("Your answer was not valid \nPlease try again")
           Input = input("Type in your answer below and then press enter\n(Acceptable answers include y, yes, no, n): ")
       if Input in yesAnswers:
           print("Ok, Lets get started")
           cashConfirm = "true"
       elif Input in noAnswers:
           print("Ok Cool. Lets Try That again.\nPress Enter")
           input("")
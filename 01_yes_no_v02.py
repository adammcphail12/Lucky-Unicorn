
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



print("\nCoolio, Lets Get Started...")
































#Varibles and Lists
valid_answers = ["yes", "y", "no", "n",]





#My Methods
class errorMessages:
    def f1():
        while Input not in valid_answers:
            print("Your answer was not valid \nPlease try again")
            Input = input("Type in your answer below and then press enter\n(Acceptable answers include y, yes, no, n): ").lower()


print("Hello, Welcome to my Game.")

#sets input and checks if its valid
Input = input("Type in your answer below and then press enter\n(Acceptable answers include y, yes, no, n) \nHave you played before? ")


errorMessages.f1()
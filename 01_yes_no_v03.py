
# Lists Used in Yes_No Checker
yes_answers = ["y","yes"]
no_answers = ["n", "no"]
valid_answers = ["n", "no","y","yes"]

# This is a reusable piece of code that the programmer can re-use whenever their is a yes/no question.

def yes_no(question,yes, no, error):
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


# Main Routine 

played_before = yes_no("Have you played before?","Allright Sweet","Here are they instructions\n---Instructions TBC---","That is not a valid answer")

print("\nOk Lets get started")

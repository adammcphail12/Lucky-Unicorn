def yes_no(question, error):
        
    valid = False
    while not valid:

        response = input (question)    

        if response == "":
            print(error)
        else:
            return response

# Main routine

played_before = yes_no("Have you played before", "Played before can't be blank")
print()
like_com = yes_no("Do you like com?", "you have to say yes to this")
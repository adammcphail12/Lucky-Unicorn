
# Reusable Number Checker tool 
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


payment = num_check("How much would you like to play with? ","Please Enter a whole number between 1 and 10\n" )
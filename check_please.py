import math

def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("whats the total? "))
    number_of_people = int(input("how many people are there? "))
except ValueError:
    print("oh no! thats not a number try again...")
    
else:
    print("each person owes ${}".format(split_check(total_due, number_of_people)))
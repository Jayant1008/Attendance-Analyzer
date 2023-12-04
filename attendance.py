l=int(input("No. of Lectures in week:"))
term=input("Enter Term('A/a' for Autumn/'S/s' for Spring):")
att=input("Attendance Marks:")

credits=l

weeks=16  # No. of working weeks for a term.

"""7 days holiday in AUTUMN term and 5 days holiday in SPRING term(As per the Official Page)"""

if term=="A" or "a":
    working_days=(weeks*5)-7
    

if term=="S" or "s":
    working_days=(weeks*5)-5
    
classes=(working_days//5)*credits #No. of classes.

print("No. of classes for your course is approximately {}.".format(classes))

def percentage(a,b):
    return (a*b)//100
if att=="5":
    print("You should attend atleast {} classes for not getting detained.".format(percentage(classes,75)))
    print("You should attend:")
    print("{} - {} classes for securing 2 MARKS".format(percentage(classes,75),percentage(classes,80)))
    print("{} - {} classes for securing 3 MARKS".format(percentage(classes,80),percentage(classes,85)))
    print("{} - {} classes for securing 4 MARKS".format(percentage(classes,85),percentage(classes,90)))
    print("{} - {}classes for securing 5 MARKS".format(percentage(classes,90),percentage(classes,100)))
if att=="15":
    print("You should attend atleast {} classes for not getting detained.".format(percentage(classes,75)))
    print("You should attend:")
    print("{} - {} classes for securing 6 MARKS".format(percentage(classes,75),percentage(classes,80)))
    print("{} - {} classes for securing 9 MARKS".format(percentage(classes,80),percentage(classes,85)))
    print("{} - {} classes for securing 12 MARKS".format(percentage(classes,85),percentage(classes,90)))
    print("{} - {}classes for securing 15 MARKS".format(percentage(classes,90),percentage(classes,100)))
if att=="20":
    print("You should attend atleast {} classes for not getting detained.".format(percentage(classes,75)))
    print("You should attend:")
    print("{} - {} classes for securing 8 MARKS".format(percentage(classes,75),percentage(classes,80)))
    print("{} - {} classes for securing 12 MARKS".format(percentage(classes,80),percentage(classes,85)))
    print("{} - {} classes for securing 16 MARKS".format(percentage(classes,85),percentage(classes,90)))
    print("{} - {}classes for securing 20 MARKS".format(percentage(classes,90),percentage(classes,100)))
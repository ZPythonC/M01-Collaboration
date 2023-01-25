#Zander Cross
#M02 Case Study
#This program will recieve input for a first name, last name, and GPA. It will then print a message based on
#whether or not the GPA is high enough for the Dean's List or Honor Roll.
lastName = input("Please enter your last name or ZZZ to quit: ")
if lastName == "ZZZ":
    print("End of Line")
else:
    firstName = input("Please enter your first name: ")
    GPA = input("Please enter your GPA: ")
    if float(GPA) >= 3.25:
        print("Congratulations! " + firstName + " " + lastName + " has made the Honor Roll!")
    if float(GPA) >= 3.5:
        print("Congratulations! " + firstName + " " + lastName + " has made the Dean's List!")
    if float(GPA) < 3.25:
        print("I'm sorry. " + firstName + " " + lastName + " has made neither the Dean's List nor the Honor Roll.")
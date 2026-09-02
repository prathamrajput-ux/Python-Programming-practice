# write a program  to determine the character entered by the user.

char = input("Press any key : ")

if(char.isalpha()):
    print("you pressed any character")

if(char.isdigit()):
    print("You pressed any digit")

if(char.isspace()):
    print("You pressed white space ")
fname = input("Enter file name: ")
#open file using with
with open(fname) as file:
    # for loop through the lines and print it
    for line in file:
        # use funtion to upper the text 
        # and change print function to not print a new line
        print(line.upper().rstrip())
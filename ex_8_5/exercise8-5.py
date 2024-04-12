fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
emails = []
with open(fname) as file:
    for line in file:
        if line.startswith("From "):
            line = line.split()
            emails.append(line[1])
            print(line[1])
            
print(f"There were {len(emails)} lines in the file with FROM as the first word", sep="\n")

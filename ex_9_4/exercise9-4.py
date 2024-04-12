fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
emails = {}
with open(fname) as file:
    for line in file:
        if line.startswith("From "):
            line = line.split()
            email = line[1]
            emails[email] = emails.get(email, 0) + 1

max_email = max(emails, key=emails.get)
print(max_email, emails[max_email])

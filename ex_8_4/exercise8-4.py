fname = input("Enter file name: ")
lines = []
words = []
with open(fname) as file:
    for line in file:
        line = line.split()
        lines += line
for word in lines:
    if word not in words:
        words.append(word)

print(sorted(words)) 


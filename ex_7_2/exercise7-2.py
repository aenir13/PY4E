fname = input("Enter file name: ")
linesum = 0
count = 0
with open(fname) as file:
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            number = line.find("0")
            linesum += float(line[number:])
            count += 1

    print("Average spam confidence:", linesum / count)
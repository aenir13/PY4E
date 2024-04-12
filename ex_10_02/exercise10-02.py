fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"

hours = {}
with open(fname) as file:
    for line in file:
        if line.startswith("From "):
            line = line.split()
            hour = line[5]
            hour = hour.split(":")
            hour = hour[0]
            hours[hour] = hours.get(hour, 0) + 1

for hour, count in sorted(hours.items()):
    print(hour, count)

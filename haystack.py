import re


def main():

    numbers = []
    with open("regex_sum_2008368.txt") as file:
        for line in file:
            number = re.findall("[0-9]+", line)
            numbers += number

    ntotal = 0
    for i in numbers:
        ntotal += int(i) 

    print(ntotal)


if __name__ == "__main__":
    main()

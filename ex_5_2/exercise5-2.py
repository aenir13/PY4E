def main():
    bignum = None
    lilnum = None
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            num = int(num)
        except:
            print("Invalid input")
            continue
        if bignum is None and lilnum is None:
            bignum = num
            lilnum = num
        if bignum < num:
            bignum = num
        if lilnum > num:
            lilnum = num
    
    print(f"Maximum is {bignum}")
    print(f"Minimum is {lilnum}")


if __name__ == "__main__":
    main()

def main():
    hrs = float(input("Hours worked: "))
    rate = float(input("Rate: "))
    print("Pay", computepay(hrs, rate))






def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r
        h -= 40
        overpay = h * (r * 1.50)
        return pay + overpay
    

if __name__ == "__main__":
    main()
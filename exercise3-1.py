hrs = float(input("Hours worked: "))
rate = float(input("Rate per hour: "))
overrate = rate * 1.5
if hrs <= 40:
    pay = hrs * rate
# if worked hour bigger than 40, deduce normal pay and calcualte overpay    
elif hrs > 40:
    pay = 40 * rate
    hrs -= 40
    overpay = hrs * overrate
print(pay + overpay) 
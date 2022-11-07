hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = 0
hours = float(hours)
rate = float(rate)
if hours <= 40:
    pay = hours * rate
else:
    pay = (40 * rate) + ((hours - 40) * rate * 1.5)
print("Pay:", round(pay,2))
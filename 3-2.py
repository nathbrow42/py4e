hours = input("Enter Hours: ")
# try to change hours to float
try:
    hours = float(hours)
except:
    print("Error, please enter numeric input")
    exit()
rate = input("Enter Rate: ")
#try to change rate to float
try:
    rate = float(rate)
except:
    print("Error, please enter numeric input")
    exit()
#init pay and calculate
pay = 0
if hours <= 40: #regular time
    pay = hours * rate
else: #overtime
    pay = (40 * rate) + ((hours - 40) * rate * 1.5)
print("Pay:", round(pay,2))
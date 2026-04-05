def computepay(hours, rate):
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        pay = hours * rate
    return pay


hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

print("Pay:", computepay(hours, rate))

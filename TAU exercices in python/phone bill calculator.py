def taxcalculate(x):
    return x/100*15


def overagefee(x):
    return x*0.25


def finaltotal(x, y):
    return x+y


planFee = int(input("Enter the call plan fee :"))
overageMinutes = int(input("Enter number of overage minutes :"))

print("Plan fee :", planFee)
print("Overage minutes fee :", overagefee(overageMinutes))
print("Sub Total :", overagefee(overageMinutes) + planFee)
print("Total :", finaltotal(taxcalculate(overagefee(
    overageMinutes) + planFee), overagefee(overageMinutes) + planFee))


low = 0
upp = 0
spe = 0
dig = 0
passwd = input("Enter password :")
if (len(passwd) >= 8):
    for i in passwd:

        # counting lowercase alphabets
        if (i.islower()):
            low += 1

        # counting uppercase alphabets
        if (i.isupper()):
            upp += 1

        # counting digits
        if (i.isdigit()):
            dig += 1

        # counting the mentioned special characters
        if (i == '@' or i == '$' or i == '_'):
            spe += 1
if (low >= 1 and upp >= 1 and spe >= 1 and dig >= 1 and low+spe+upp+dig == len(passwd)):
    print("Valid Password")
else:
    print("Invalid Password")

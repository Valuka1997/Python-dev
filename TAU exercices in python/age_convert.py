def age_convert():
    ageinp = int(input("Enter your age : "))
    agesec = ageinp * 365 * 24 * 60 * 60
    print("You lived {} seconds on earth".format(agesec))


age_convert()
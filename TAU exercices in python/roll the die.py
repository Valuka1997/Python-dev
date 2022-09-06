import random

increment = 0
space = 0
while (increment < 5):
    die = random.randint(1, 6)
    print("Your die has rolled to number ", die)
    space += die
    print("you have to advance ", 20-space, "spaces")
    if (space > 20):
        print("You advanced more than 20 spaces. you lose!")
        break
    elif (space == 20):
        print("Congratulations you won!")
    else:
        print("you advanced to space ", space)
    increment += 1
if (space != 20):
    print("You lose!")

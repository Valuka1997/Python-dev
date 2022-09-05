import random

mgnu = random.randint(0, 10)
print("Enter your lucky number between 0-10 :")
num = int(input())
if (num == mgnu):
    {
        print("Congratulations you won!!!")
    }
else:
    {
        print("Winning number is", mgnu, "Better luck next time.Try again!")
    }

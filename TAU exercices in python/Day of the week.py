arr = ['Monday', 'Tuesday', 'Wednesday',
       'Thursday', 'Friday', 'Saturday', 'Sunday']
day = int(input("Enter the number corresponding to the day of week :"))
if(day<7):
       if(day>0):
              print(arr[day-1])
       else:
              print("Enter a valid number")

else:
       print("Enter a valid number")

from token import GREATER


user1 = int(input("enter the number1: "))
user2 = int(input("enter the number2: "))
user3 = int(input("enter the number3: "))
user4 = int(input("enter the number4: "))

if (user1>user2):
    f1 = user1
else:
    f1 = user2

if (user3>user4):
    f2 = user3
else:
    f2 = user4

if (f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")    


# this is the formatt to execute the greatest no. 

try:

    a = int(input("enter the number: "))
    c = 2/a 
    print(c)

except ValueError as e:
    print("please enter the valid number")

except ZeroDivisionError as e:
    print("make sure you are not dividing by zero")

print("thanks for visiting this page")    

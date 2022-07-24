# try with finally 
try:
    i = int(input("enter the number:  "))
    f = 3/i

except Exception as e:
    print(e)    
    exit()

finally:
    print("we are sucessful")    
    

# this method is used for, no matter what is the input but programme must be go on .
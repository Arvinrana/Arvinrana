# try with else method
try:
    i = int(input("enter the number:  "))

    f = 1/i

except Exception as e:
    print(e)    

else:
    print("we are sucessful")    
    

# this is else method is used for , if user print invalid no. it will  not process further     
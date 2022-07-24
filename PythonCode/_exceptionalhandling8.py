# global function 

a = 41120   #   this is global variable whenever you want global value you have to mention it ."global" example given
            #  it will  not execute

def num():
    global a
    print(f"statement 1 : {a}") 
    a = 78   #   this is local variable . you can call it without mention  "local variable" 
    print(f"statement 2 : {a}")

num()
print(f"statement 3 : {a}")    


#  understand 

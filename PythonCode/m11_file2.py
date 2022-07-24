def greet(name):
    print(f"good morning {name}")

# print(__name__)    
if __name__== "__main__":
    n = input("enter your name: ")
    greet(n)

# this module describe that this programme ran from main file . and  dont want to ran this user input function 
# run in another file. it will will directly run without asking the input 
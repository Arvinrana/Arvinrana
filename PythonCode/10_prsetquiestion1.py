class Programmer:             # |   this is class 
    company = "microsoft"     # |

    def __init__(self, name, product):   # |  this is constuctor function  which helps to construct the details form
        self.name = name                 # |
        self.product = product           # |

    def getInfo(self):     # this is getinfo function    ( f - a key, which helps to insert a value in {} bracket  )
        print(
            f"the name of the company is {self.company} and the name of Programmer is {self.name} and the product is {self.product}")

arvin = Programmer("arvin", "ml")   # this is object 
kaka = Programmer("kaka", "AI")  
arvin.getInfo() 
kaka.getInfo()

#  understood .....

class calculator:
    def __init__(self, num):
        self.number = num 

    def square(self):
        print(f"the value of {self.number} square is {self.number **2}")

    def squareroot(self):
        print(f"the value of {self.number} square is {self.number **0.5}")    

    def squarecube(self):
        print(f"the value of {self.number} square is {self.number **3}")  

    @staticmethod
    def greet():
        print("welcome to arvin's calculator machine ")

a = calculator(6) 
a.greet()       
a.square()
a.squareroot()
a.squarecube()


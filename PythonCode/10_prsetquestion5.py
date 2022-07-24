class train:

    def __init__(self, name, seats, fare):
        self.fare = fare
        self.name = name
        self.seats = seats

    def getStatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the seats avaialbe in the train are {self.seats}")

    def fareInfo(self):
        print(f"the price of the ticket is rs.{self.fare}")


rajdhani = train("rajhdhani express: 14528" , 49, 500)   
rajdhani.getStatus()
rajdhani.fareInfo()


# question done 

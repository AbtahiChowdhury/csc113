class Restaurant():
    def __init__(self, name, cuisinetype):
        self.name=name
        self.cuisinetype=cuisinetype
        self.numberserved=0
    def describeRestaurant(self):
        print("This restaurant is called {} and sells {} food.".format(self.name,self.cuisinetype))
    def openRestaurant(self):
        print("{} is now open".format(self.name))
    def setNumberServed(self,numserved):
        self.numberserved=numserved
    def incrementNumberServed(self,numserved):
        self.numberserved+=numserved
    def printNumberServed(self):
        print("{} has served {} people.".format(self.name,self.numberserved))

restaurant=Restaurant('Akino','Japanese')
restaurant.printNumberServed()
restaurant.setNumberServed(100)
restaurant.printNumberServed()
restaurant.incrementNumberServed(25)
restaurant.printNumberServed()
class Restaurant():
    def __init__(self, name, cuisinetype):
        self.name=name
        self.cuisinetype=cuisinetype
    def describeRestaurant(self):
        print("This restaurant is called {} and sells {} food.".format(self.name,self.cuisinetype))
    def openRestaurant(self):
        print("{} is now open".format(self.name))

class IceCremeStand(Restaurant):
    def __init__(self,name,listofflavors):
        super(IceCremeStand,self).__init__(name,'Ice Creme')
        self.flavors=listofflavors
    def printFlavors(self):
        print(self.flavors)
    

restaurant=IceCremeStand('IcE cReMe',['vanilla','chocolete'])
restaurant.printFlavors()
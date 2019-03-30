class Restaurant():
    def __init__(self, name, cuisinetype):
        self.name=name
        self.cuisinetype=cuisinetype
    def describeRestaurant(self):
        print("This restaurant is called {} and sells {} food.".format(self.name,self.cuisinetype))
    def openRestaurant(self):
        print("{} is now open".format(self.name))


somefineeatery=Restaurant('Akino','Japanese')
print("{} is a {} restaurant".format(somefineeatery.name,somefineeatery.cuisinetype))
somefineeatery.describeRestaurant()
somefineeatery.openRestaurant()
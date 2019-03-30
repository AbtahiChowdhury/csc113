class Restaurant():
    def __init__(self, name, cuisinetype):
        self.name=name
        self.cuisinetype=cuisinetype
    def describeRestaurant(self):
        print("This restaurant is called {} and sells {} food.".format(self.name,self.cuisinetype))
    def openRestaurant(self):
        print("{} is now open".format(self.name))


somefineeatery1=Restaurant('Akino','Japanese')
somefineeatery2=Restaurant('Kahlil','Bengali')
somefineeatery3=Restaurant('Marivilla','Ecuadorian')

somefineeatery1.describeRestaurant()
somefineeatery2.describeRestaurant()
somefineeatery3.describeRestaurant()
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometerreading=0
    def getDescriptiveName(self):
        longname=str(self.year)+' '+self.make+' '+self.model
        return longname.title()
    def readOdometer(self):
        print("This car has "+str(self.odometerreading)+" miles on it.")
    def updateOdometer(self,mileage):
        if mileage>=self.odometerreading:
            self.odometerreading=mileage
        else:
            print("You can't roll back an odometer!")
    def incrementOdometer(self,miles):
        self.odometerreading+=miles

class Battery():
    def __init__(self,batterysize=70):
        self.batterysize=batterysize
    def describeBattery(self):
        print("This car has a "+str(self.batterysize)+"-kWh battery.")
    def getRange(self):
        if self.batterysize==70:
            range=240
        elif self.batterysize==85:
            range=270
        print("This car can go approximately "+str(range)+" miles on a full charge.")
    def upgradeBattery(self):
        if self.batterysize!=85:
            self.batterysize=85

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super(ElectricCar,self).__init__(make,model,year)
        self.battery=Battery()
    def describeBattery(self):
        self.battery.describeBattery()
    def getRange(self):
        self.battery.getRange()
    def upgradeBattery(self):
        self.battery.upgradeBattery()

mytesla=ElectricCar('tesla','model s','2016')
print(mytesla.getDescriptiveName())
mytesla.describeBattery()
mytesla.getRange()
mytesla.upgradeBattery()
mytesla.describeBattery()
mytesla.getRange()
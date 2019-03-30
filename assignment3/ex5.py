class User():
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        self.loginattempts=0
    def incrementLoginAttempts(self):
        self.loginattempts+=1
    def resetLoginAttempts(self):
        self.loginattempts=0
    def printLoginAttempts(self):
        print('{} attempted to login {} times.'.format(self.firstname,self.loginattempts))

user1=User('Riccarda','McRae')
user1.printLoginAttempts()
user1.incrementLoginAttempts()
user1.incrementLoginAttempts()
user1.incrementLoginAttempts()
user1.incrementLoginAttempts()
user1.incrementLoginAttempts()
user1.printLoginAttempts()
user1.resetLoginAttempts()
user1.printLoginAttempts()
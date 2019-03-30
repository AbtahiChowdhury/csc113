class User():
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def describeUser(self):
        print("{} {} is a user and is {} years old.".format(self.firstname,self.lastname,self.age))
    def greetUser(self):
        print("Welcome {} {}.".format(self.firstname,self.lastname))


user1=User('Riccarda','McRae',18)
user2=User('Purnima','Wirth',17)
user3=User('David','Avinash',19)
user4=User('Emmi','Gjorgiev',20)
user5=User('Padma','Ueno',18)

user1.greetUser()
user1.describeUser()
user2.greetUser()
user2.describeUser()
user3.greetUser()
user3.describeUser()
user4.greetUser()
user4.describeUser()
user5.greetUser()
user5.describeUser()
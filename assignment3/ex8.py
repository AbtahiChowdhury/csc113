class User():
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def describeUser(self):
        print("{} {} is a user and is {} years old.".format(self.firstname,self.lastname,self.age))
    def greetUser(self):
        print("Welcome {} {}.".format(self.firstname,self.lastname))

class Privileges():
    def __init__(self,listofprivileges):
        self.listofprivileges=listofprivileges
    def showPrivileges(self):
        print(self.listofprivileges)

class Admin(User):
    def __init__(self,firstname,lastname,age,listofprivileges):
        super(Admin,self).__init__(firstname,lastname,age)
        self.listofprivileges=Privileges(listofprivileges)
    def showPrivileges(self):
        self.listofprivileges.showPrivileges()

admin=Admin("Aleah","MacGinnis",21,["can delete post","can ban users"])
admin.showPrivileges()
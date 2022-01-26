# Create a data structure that can store data for million users. Ensure you can insert, delete or modify user data
# NOTE: The usernames are unique
# complexity of the program is O(N) - This applies to the brute force solution before application of the binary
#                                      search tree algorithm

# signature class
# Add a constructor method to allow storage of use data
# __REPR__ and __STR__(string format) are used to automate the printing of results
class Users:
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email

    # Method greeting
    # def __repr__(self):
    #    return ('Hi i am {} and my email is {}'.format(self.name,self.email))
    # def __str__(self):
    #    return self.__repr__()

# Users database that inherits from the users class
# It contains methods required to modify or store user data
class Database:
    def __init__(self):
        self.database = []

    def insert(self,user):
        index = 0
        if len(self.database) == 0:
            self.database.insert(index,user)
        while index < len(self.database):
            if self.database[index].username > user.username:
                break
            index+=1
        self.database.insert(index,user)
        return self.database

    def find(self, username):
        for i in self.database:
            if i.username == username:
                print(i)
                return i

    def list_all(self):
        print(self.database)
        return self.database

    def update(self, user):
        target = self.find(user.name)
        target.name, target.email = user.name, user.email

# Create an instance of the object created
user1 = Users('john','jonathan maingi','john@gmail.com')
user2 = Users('amin','aminata oku','amin@gmail.com')
user3 = Users('ken','kenneth michuki','ken@gmail.com')
user4 = Users('paul','paul gitengi','paul@gmail.com')
user5 = Users('raul','raul nose','raul@gmail.com')


users_database = Database()

users_database.insert(user1)
users_database.insert(user2)
users_database.insert(user4)
users_database.find('john')

users_database.list_all()

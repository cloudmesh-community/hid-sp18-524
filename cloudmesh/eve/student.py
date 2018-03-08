class Student(object):
    def __init__(self, firstname, lastname, university, email):
        self.firstname = firstname
        self.lastname = lastname
        self.university = university
        self.email = email
        self.username = 'undefined'

    def get(self):
        return self.__dict__

    def setUsername(self, name):
        self.username = name
        return name

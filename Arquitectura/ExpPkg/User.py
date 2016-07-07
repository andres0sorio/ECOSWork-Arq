
class User(object):
    def __init__(self):
        """standard constructor"""
        self.identificationNumber = 0
        self.userProfile = "patient"
        self.name = "A"
        self.lastName = "Z"
        self.email = "xx@xx"
        self.password = "xxxx"

    def setIdentificationNumber(self, identificationNumber):
        self.identificationNumber = identificationNumber

    def setUserProfile(self, userProfile):
        self.userProfile = userProfile

    def setName(self, name):
        self.name = name

    def setLastName(self, lastName):
        self.lastName = lastName

    def setEmail(self,email):
        self.email = email

    def setPassword(self,password):
        self.password = password

    def getData(self):
        line = []
        line.append(str(self.identificationNumber))
        line.append(self.userProfile)
        line.append(self.name)
        line.append(self.lastName)
        line.append(self.email)
        line.append(self.password)
        return ','.join(line)

    def getIdentificationNumber(self):
        return self.identificationNumber
        
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

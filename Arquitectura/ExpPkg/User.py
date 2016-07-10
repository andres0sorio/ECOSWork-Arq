
class User(object):
    def __init__(self):
        """standard constructor"""
        self.identification = 0
        self.user_profile = "user"
        self.name = "A"
        self.last_name = "Z"
        self.email = "xx@xx"
        self.password = "xxxx"
        self.salt = "xacx"

    def setIdentificationNumber(self, identificationNumber):
        self.identification = identificationNumber

    def setUserProfile(self, userProfile):
        self.user_profile = userProfile

    def setName(self, name):
        self.name = name

    def setLastName(self, lastName):
        self.last_name = lastName

    def setEmail(self,email):
        self.email = email

    def setPassword(self,password):
        self.password = password

    def setSalt(self,salt):
        self.salt = salt

    def getData(self):
        line = []
        line.append(str(self.identification))
        line.append(self.user_profile)
        line.append(self.name)
        line.append(self.last_name)
        line.append(self.email)
        line.append(self.password)
        line.append(self.salt)
        return ','.join(line)

    def getIdentificationNumber(self):
        return self.identification
        
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

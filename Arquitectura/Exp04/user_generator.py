from faker import Factory
import datetime
import time 
import random
import time
import sys
sys.path.append('../')
from ExpPkg import JsonEpisodeHelper
from ExpPkg import User

perfil = ['user']

input1 = 'simulated_records.dat'
input2 = 'user_simulated_records.dat'

##password before encription: asd123
salt = "3093f560-16dc-4da5-8243-c55edf9f6ba0"
password = "1508ef045ef6b5c77dd9e272d3fd3892c0b668a41aa4b2b5f878cc9a9d11b811"

def generatePwd():
    pwd = ''.join(random.choice('0123456789abcde') for i in range(6))
    return pwd
    
def selectFromList(names):
    lucky_name = random.choice(names)
    return lucky_name
            
if __name__ == "__main__":

    cedulas = []
    cedula_ant = 0
    with open(input1) as inputfile:
        for line in inputfile:
            data = line[:-1].split(',')
            cedula = int(data[0])
            if cedula != cedula_ant:
                cedulas.append(cedula)
                cedula_ant = cedula
            else:
                continue

    index = 0
    
    
    with open(input2) as inputfile:
        for line in inputfile:
            data = line[:-1].split(',')
            full_name = data[0].split()
            email = data[1]
            rol = perfil[0]
            name = []
            pwd = generatePwd()
            for item in full_name:
                if item.find('.') <= 0:
                    name.append(item)
                if len(name) >= 2:
                    break

            #print cedulas[index], name[0], name[1], email, rol, pwd
            user = User()
            user.setIdentificationNumber(cedulas[index])
            user.setUserProfile(rol)
            user.setName( name[0] )
            user.setLastName( name[1] )
            user.setEmail( email )
            user.setPassword( password )
            user.setSalt( salt )
            print user.__dict__
            
            index += 1
            

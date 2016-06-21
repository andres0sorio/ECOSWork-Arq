from Migrana import Migrana

class Episodio(object):
    def __init__(self):
        """standard constructor"""
        self.iD = 0
        self.nombre = "Xxxx"
        self.apellido = "Xxxx"
        self.migrana = Migrana()

    def setID(self, id):
        self.iD = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setMigrana(self, migrana):
        self.migrana = migrana

    def getID(self):
        return self.iD 

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getMigrana(self):
        return self.migrana

    
    

class Migrana(object):
    def __init__(self):
        self.iD = 0
        self.fecha = "OOOOOO"
        self.nivel = 0
        self.localizacion = 0
        self.medicamento = "Dolex"

    def setID(self, id):
        self.iD = id

    def setFecha(self, fecha):
        self.fecha = fecha

    def setNivel(self,nivel):
        self.nivel = nivel

    def setLocalizacion(self,localizacion):
        self.localizacion = localizacion

    def setMedicamento(self,medicamento):
        self.medicamento = medicamento

    def getiD(self):
        return self.iD

    def getFecha(self):
        return self.fecha

    def getNivel(self):
        return self.nivel 

    def getLocalizacion(self):
        return self.localizacion 

    def getMedicamento(self):
        return self.medicamento

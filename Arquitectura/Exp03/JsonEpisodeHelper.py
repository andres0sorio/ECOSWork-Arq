
class JsonEpisodeHelper(object):
    def __init__(self):
        """standard constructor"""
        self.id = 0
        self.cedula = 0
        self.fecha = 'XXXX/XXXX'
        self.hora = 'X:X:X'
        self.nivelDolor = 0
        self.intensidad = 0

    def setID(self, id):
        self.iD = id

    def setCedula(self, cedula):
        self.cedula = cedula

    def setFecha(self, fecha):
        self.fecha = fecha

    def setHora(self, hora):
        self.hora = hora

    def setNivel(self, nivel):
        self.nivelDolor = nivel

    def setIntensidad(self,intensidad):
        self.intensidad = intensidad


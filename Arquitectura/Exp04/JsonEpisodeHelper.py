class JsonEpisodeHelper(object):
    """
    """
    def __init__(self):
        """standard constructor"""
        self.cedula = 0
        self.fecha = 'XXXX/XXXX'
        self.hora = 'X:X:X'
        self.nivelDolor = 0
	self.medicamento = 'A'
        self.actividad = 'xx'

    def setCedula(self, cedula):
        self.cedula = cedula

    def setFecha(self, fecha):
        self.fecha = fecha

    def setHora(self, hora):
        self.hora = hora

    def setNivel(self, nivel):
        self.nivelDolor = nivel

    def setMedicamento(self,medicamento):
        self.medicamento = medicamento

    def setActividad(self,actividad):
        self.actividad = actividad

    def getData(self):
        line = []
        line.append(str(self.cedula))
        line.append(self.fecha)
        line.append(self.hora)
        line.append(str(self.nivelDolor))
        line.append(self.medicamento)
        line.append(self.actividad)
        return ','.join(line)
        

from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, nombre, fecha_de_nacimiento, direccion):
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.direccion = direccion

    @abstractmethod
    def aceptar(self, visitante):
        pass

class ClienteIndividual(Cliente):
    def aceptar(self, visitante):
        visitante.visitar_cliente_individual(self)

class ClienteCorporativo(Cliente):
    def aceptar(self, visitante):
        visitante.visitar_cliente_corporativo(self)

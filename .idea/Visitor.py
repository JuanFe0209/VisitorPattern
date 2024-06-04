from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visitar_cliente_individual(self, cliente):
        pass

    @abstractmethod
    def visitar_cliente_corporativo(self, cliente):
        pass

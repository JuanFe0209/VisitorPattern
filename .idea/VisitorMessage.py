from Visitor import Visitor
class VisitorMessage(Visitor):
    def visitar_cliente_individual(self, cliente):
        print(f"Enviando mensaje individual a {cliente.nombre} en {cliente.direccion}")

    def visitar_cliente_corporativo(self, cliente):
        print(f"Enviando mensaje corporativo a {cliente.nombre} en {cliente.direccion}")

from Cliente import ClienteIndividual
from Cliente import ClienteCorporativo
from VisitorMessage import VisitorMessage
if __name__ == "__main__":
    cliente_individual = ClienteIndividual("Juan Felipe", "2003-02-09", "Calle 5N")
    cliente_corporativo = ClienteCorporativo("Empresa Microsoft", "1990-01-01", "Calle 2 avenida 11")

    visitorMessage = VisitorMessage()

    cliente_individual.aceptar(visitorMessage)
    cliente_corporativo.aceptar(visitorMessage)

from Client import Client


class Llibreta:
    def __init__(self):
        self.llista_clients = []
        self.id_client_comptador = 1

    def get_llista_clients(self):
        for client in self.llista_clients:
            print(client)

    def afegir_client(self, nom, cognom, telefon, correu, adreca, codi_postal, ciutat, provincia, pais):
        identificador = self.id_client_comptador  # Utilizamos el contador de identificadores
        self.id_client_comptador += 1  # Incrementamos el contador para el siguiente cliente

        client_nou = Client(identificador, nom, cognom, telefon, correu, adreca, codi_postal, ciutat, provincia, pais)
        self.llista_clients.append(client_nou)

    def eliminar_client(self, identificador):
        for client in self.llista_clients:
            if client.identificador == identificador:
                self.llista_clients.remove(client)
                print("Client eliminat.")
                return
        print("No s'ha trobat cap client amb aquest identificador.")

    def cercar_per_id(self, identificador):
        for client in self.llista_clients:
            if client.identificador == identificador:
                return [client]
        return []

    def cercar_per_nom(self, nom):
        resultats = []
        for client in self.llista_clients:
            if client.nom.lower() == nom.lower():
                resultats.append(client)
        return resultats

    def cercar_per_cognom(self, cognom):
        resultats = []
        for client in self.llista_clients:
            if client.cognom.lower() == cognom.lower():
                resultats.append(client)
        return resultats


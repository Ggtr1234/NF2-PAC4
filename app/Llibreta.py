class Llibreta:
    def __init__(self,id_client):
        self.id_client = id_client
        self.llista_clients = []

    def get_llista_clients(self):
        return self.llista_clients

    def afegir_client(self, client):
        self.clients.append(client)
        print(f"Client afegit: {client}")

    def eliminar_client (self, id_client):
        for client in self.llista_clients:
            if client.id_client == id_client:
                self.llista_clients.remove(client)
                print(f"Client eliminado: {client}")
    def cercar_per_id_client(self,id_client):
        for client in self.llista_clients:
            if client.id_client == id_client:
                return [client]

    def cercar_per_nombre_client(self,nombre_client):
        for client in self.llista_clients:
            if client.nombre_client == nombre_client:
                return [client]

    def cercar_per_cognom_client(self,cognom_client):
        for client in self.llista_clients:
            if client.cognom_client == cognom_client:
                return [client]
class Llibreta:
    def __init__(self,id_client):
        self.id_client = id_client
        self.llista_clients = []

    def get_llista_clients(self):
        return self.llista_clients

    def afegir_client(self):

class Client:
    def __init__(self, identificador, nom, cognom, telefon, correu, adreca, codi_postal, ciutat, provincia, pais):
        self.identificador = identificador
        self.nom = nom
        self.cognom = cognom
        self.telefon = telefon
        self.correu = correu
        self.adreca = adreca
        self.codi_postal = codi_postal
        self.ciutat = ciutat
        self.provincia = provincia
        self.pais = pais

    def __str__(self):
        return f"ID: {self.identificador}, Nom: {self.nom}, Cognom: {self.cognom}, Telèfon: {self.telefon}, Correu: {self.correu}, Adreca: {self.adreca}, CodiPostal: {self.codi_postal}, Provincia: {self.provincia}, Pais: {self.pais}"

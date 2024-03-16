from Llibreta import Llibreta
class Aplicacio:
    def __init__(self):
        self.llibreta = Llibreta(0)
    def run(self):
        self.mostrar_menu_principal()
        while True:
            opcio = int(input("Opcio: "))
            if opcio == '1':
                Llibreta.afegir_client()
    def mostrar_menu_principal(self):
            print("============================")
            print("Menu principal")
            print("============================")
            print("Tria una opcio i prem Intro")
            print("============================")
            print("1. Afegir client")
            print("2. Eliminar client")
            print("3. Consultar client")
            print("4. Modificar un camp d'un client")
            print("5. Sortir")
            print("")




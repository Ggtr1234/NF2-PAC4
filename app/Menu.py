class Menu:
    @staticmethod
    def mostrar_menu_principal():
        print("Gestió de clients:")
        print("===========================")
        print("Tria una opcio y prem Intro")
        print("===========================")
        print("1. Afegir client")
        print("2. Consultar clients")
        print("3. Modificar client")
        print("4. Eliminar client")
        print("5. Sortir")
        opcio = input("OpciO: ")
        return opcio

    @staticmethod
    def mostrar_menu_consulta():
        print("Consulta de clients:")
        print("===========================")
        print("Tria una opcio y prem Intro")
        print("===========================")
        print("1. Mostrar tots els clients")
        print("2. Cerca client per nom")
        print("3. Cerca client per cognom")
        print("4. Tornar al menú principal")
        opcio = input("Opcio: ")
        return opcio



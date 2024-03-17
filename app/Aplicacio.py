from Menu import Menu
from Llibreta import Llibreta

def main():
    menu = Menu()
    llibreta_clients = Llibreta()

    while True:
        opcio_principal = menu.mostrar_menu_principal()

        if opcio_principal == '1':
            nom = input("Introdueix el nom del client: ")
            cognom = input("Introdueix el cognom del client: ")
            telefon = input("Introdueix el telèfon del client: ")
            correu = input("Introdueix el correu electrònic del client: ")
            adreca = input("Introdueix l'adreça del client: ")
            codi_postal = input("Introdueix el codi postal del client: ")
            ciutat = input("Introdueix la ciutat del client: ")
            provincia = input("Introdueix la província del client: ")
            pais = input("Introdueix el país del client: ")
            llibreta_clients.afegir_client(nom, cognom, telefon, correu, adreca, codi_postal, ciutat, provincia, pais)

        elif opcio_principal == '2':
            opcio_consulta = menu.mostrar_menu_consulta()
            if opcio_consulta == '1':
                llibreta_clients.get_llista_clients()
            elif opcio_consulta == '2':
                nom = input("Introdueix el nom del client a cercar: ")
                resultats = llibreta_clients.cercar_per_nom(nom)
                for client in resultats:
                    print(client)
            elif opcio_consulta == '3':
                cognom = input("Introdueix el cognom del client a cercar: ")
                resultats = llibreta_clients.cercar_per_cognom(cognom)
                for client in resultats:
                    print(client)

        elif opcio_principal == '3':
            identificador = int(input("Introdueix l'identificador del client a modificar: "))
            resultats = llibreta_clients.cercar_per_id(identificador)
            if resultats:
                print("Dades del client:")
                for client in resultats:
                    print(client)
            else:
                print("No s'ha trobat cap client amb aquest identificador.")

        elif opcio_principal == '4':
            identificador = int(input("Introdueix l'identificador del client a eliminar: "))
            llibreta_clients.eliminar_client(identificador)

        elif opcio_principal == '5':
            print("Adéu!")
            break

        else:
            print("Opció no vàlida. Torna a introduir una opció.")

if __name__ == "__main__":
    main()
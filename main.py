from socio import Socio, Base
from sqlalchemy import create_engine

def menu():
    print ("**** MENU DE OPCIONES *****")
    print("Opcion 1: Agregar cliente")
    print("Opcion 2: Mostrar datos del cliente")
    print("Opcion 0: Salir")


if __name__ == "__main__":
    engine= create_engine("sqlite:///socios.db")
    Base.metadata.create_all(engine)

    menu()
    opc= int(input("Ingrese opcion: "))
    while opc != 0:
        if opc== 1:
            socio= Socio.crear_socio()
            socio.guardar_socio(engine)
        elif opc== 2:
            dni= input("Ingrese DNI del socio: ")
            Socio.mostrar_socios(engine, dni)
        print("")
        menu()
        opc= int(input("Ingrese opcion: "))

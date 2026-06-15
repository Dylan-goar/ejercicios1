def mostrar_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|1| Agregar Mascota      ||")
    print("|2| Buscar Mascota       ||")
    print("|3| Eliminar Mascota     ||")
    print("|4| Marcar como Vacunada ||")
    print("|5| Mostrar Mascosas     ||")
    print("|6| Salir                ||")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una Opcion: "))
            if opcion < 1 or opcion > 6:
                print("Solo seleccione una opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar solo numeros") 
    return opcion




lista_mascota = []

op = 0

while op != 6:
    mostrar_menu()
    op = ingresar_opcion()










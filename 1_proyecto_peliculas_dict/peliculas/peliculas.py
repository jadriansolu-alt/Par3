import funciones

pelis={
    "Nombre": "toy story 5",
    "Duración":"120 minutos",
    "Idioma":"Español",
    "Clasificacion":"A",
    "Genero":"animada"
    }
      
def menuPrincipal():
    print("\n\t\t---=== MENÚ PRINCIPAL ===---\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t---=== AGREGAR CARACTERÍSTICA ===---\n")
    caracteristica=input("Introduce el nombre de la característica: ").lower().strip()
    valor=input("Introduce el valor: ").upper().strip()
    pelis[caracteristica]=valor
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t---=== CARACTERÍSTICAS DE LA PELÍCULA ===---\n")
    if len(pelis)>0:
        print("\tCaracterística\t\tValor\n")

        for i in pelis:
            print(f"{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("¡Ups! No se encontró la película. ¡Verifica de nuevo!")
    
def limpiarPeliculas(pelis):
    if len(pelis)>0:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Seguro que deseas limpiar toda la lista (Si/No)? ").lower().strip()
        if opc=="si":
            pelis=pelis.clear()
            funciones.accionExitosa()
    else:
        input("¡No hay características para borrar!") 
        
def buscarPeliculas(pelis):
    print("\n\t\t---=== BUSCAR CARACTERÍSTICA ===---\n")
    caracteristica=input("Escribe la característica que buscas: ").lower().strip()

    noencontro=False
    print("\tCaracterística\t\tValor\n")
    for i in pelis:
        if caracteristica==i:
            print("\tCaracterística\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            noencontro=True
        funciones.espereTecla()
    if not(noencontro):
        input("¡No se encontró la característica solicitada!")

def borrarPeliculas(pelis):
    print("\n\t\t---=== BORRAR CARACTERÍSTICA ===---\n")

    caracteristica = input("Escribe la característica a eliminar: ").lower().strip()

    if caracteristica in pelis:

        print("\tCaracterística\t\tValor\n")
        print(f"{caracteristica}\t\t{pelis[caracteristica]}")

        opc = ""

        while opc not in ("si", "no"):
            opc = input("¿De verdad deseas borrar esta característica (Si/No)? ").lower().strip()

        if opc == "si":
            pelis.pop(caracteristica)
            funciones.accionExitosa()

    else:
        input("¡La característica ingresada no existe!")

               
def modificarPeliculas(pelis):
    print("\n\t\t---=== MODIFICAR CARACTERÍSTICA ===---\n")

    caracteristica = input("Escribe la característica que deseas cambiar: ").lower().strip()

    noencontro = True

    for i in pelis:
        if caracteristica == i:

            print("\tCaracterística\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")

            opc = ""

            while opc != "si" and opc != "no":
                opc = input("¿Quieres cambiar el valor de esta característica (Si/No)? ").lower().strip()

            if opc == "si":
                pelis[caracteristica] = input("Escribe el nuevo valor: ").upper().strip()
                funciones.accionExitosa()

            noencontro = False
            break

    if noencontro:
        input("¡No pudimos encontrar esa característica, verifica!")
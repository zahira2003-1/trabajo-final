import random

print("=========================================")
print("INGRESASTE AL PORTAL PARA GENERAR TICKETS")
print("=========================================")

tickets = {}

def alta():
    while True:
        print("\n--- ALTA DE TICKET ---")
        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Problema: ")

        nro = random.randint(1000, 9999)
        tickets[nro] = (nombre, sector, asunto, problema)

        print("\nTICKET GENERADO")
        print("Número:", nro)
        print("Nombre:", nombre)
        print("Sector:", sector)
        print("Asunto:", asunto)
        print("Problema:", problema)
        print("¡Recordá tu número!")

        with open("tickets_guardados.txt", "a") as archivo:
            archivo.write(str(nro) + "\n")

        seguir = input("\n¿Querés generar otro ticket? (s/n): ").lower()
        if seguir != "s":
            break

def leer():
    print("\n--- LECTURA DE TICKET ---")

    if len(tickets) == 0:
        print("Todavía no hay tickets generados.")
        return
    else:
        print("Tickets disponibles:", list(tickets.keys()))

    try:
        nro = int(input("Ingresá el número de ticket: "))
    except:
        print("Ingresá solo números.")
        return

    if nro in tickets:
        n, s, a, p = tickets[nro]
        print("\nTICKET", nro)
        print("Nombre:", n)
        print("Sector:", s)
        print("Asunto:", a)
        print("Problema:", p)
    else:
        print("No existe ese ticket.")

while True:
    print("\n1) Alta de nuevo ticket")
    print("2) Leer ticket")
    print("3) Salir")

    op = input("Opción: ")

    if op == "1":
        alta()
    elif op == "2":
        leer()
    elif op == "3":
        confirmar = input("¿Confirmar? (s/n): ").lower()
        if confirmar == "s":
            print("Programa finalizado.")
            break
        else:
            print("Redirigiendo al menu principal...")

    else:
        print("Opción inválida.")

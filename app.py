tareas = []

def mostrar_tareas():
    if len(tareas) == 0:
        print("No hay tareas")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def agregar_tareas():
    taeritas= input("Agrege las tareas: ")
    tareas.append(taeritas)



def menu():
    while True:
        print("\n=== APP DE TAREAS DEL EQUIPO ===")
        print("1. Ver tareas")
        print("2. Agregar tareas")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":

            agregar_tareas()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

menu()
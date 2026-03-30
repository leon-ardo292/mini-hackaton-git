tareas = []

def mostrar_tareas():
    if len(tareas) == 0:
        print("No hay tareas")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def menu():
    while True:
        print("\n=== GESTOR DE TAREAS ===")
        print("1. Ver tareas")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

menu()
tareas = []

def agregar_tarea(tareas):
    texto = input("Escribe la nueva tarea: ")
    nueva_tarea = {"texto": texto, "completada": False}
    tareas.append(nueva_tarea)
    print("Tarea agregada correctamente.")

def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, start=1):
            estado = "✅" if tarea["completada"] else "❌"
            print(f"{i}. {tarea['texto']} {estado}")

def completar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas para completar.")
        return

    mostrar_tareas(tareas)
    numero = int(input("Ingresa el número de la tarea que quieres completar: "))

    if numero >= 1 and numero <= len(tareas):
        tareas[numero - 1]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Número inválido.")

while True:
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_tareas(tareas)
    elif opcion == "2":
        agregar_tarea(tareas)
    elif opcion == "3":
        completar_tarea(tareas)
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")

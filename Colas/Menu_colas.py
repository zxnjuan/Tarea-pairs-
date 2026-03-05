# Allison Farias y Juan Pinzon :D - 04/03/2026

from queue import Queue
import random

cola = Queue()

def esta_vacia():
    if cola.empty():
        print("😮 La cola está vacía")
    else:
        print("😊 La cola NO está vacía")

def agregar():
    valor = int(input("Ingresa el número que deseas agregar: "))
    cola.put(valor)
    print("✅ Elemento agregado correctamente")

def eliminar():
    if cola.empty():
        print("⚠️ No se puede eliminar, la cola está vacía")
    else:
        print("🗑 Se eliminó:", cola.get())

def mostrar_frente():
    if cola.empty():
        print("⚠️ La cola está vacía")
    else:
        print("🔹 Frente:", cola.queue[0])

def mostrar_final():
    if cola.empty():
        print("⚠️ La cola está vacía")
    else:
        print("🔹 Final:", cola.queue[-1])

def mostrar_datos():
    if cola.empty():
        print("⚠️ La cola está vacía")
    else:
        print("📋 Elementos:", list(cola.queue))

def contar():
    print("🔢 Cantidad de elementos:", cola.qsize())

def mayor():
    if cola.empty():
        print("⚠️ La cola está vacía")
    else:
        print("🏆 Número mayor:", max(cola.queue))

def copiar():
    if cola.empty():
        print("⚠️ La cola está vacía. No se puede copiar.")
    else:
        copia = Queue()
        
        for elemento in cola.queue:
            copia.put(elemento)
        
        print("📋 Cola original:", list(cola.queue))
        print("📄 Nueva cola creada (copia):", list(copia.queue))
        print("✅ La copia se realizó correctamente.")

def mezclar():
    if cola.empty():
        print("⚠️ La cola está vacía.")
    else:
        print("📋 Cola original:", list(cola.queue))
        
        lista = list(cola.queue)
        random.shuffle(lista)
        
        cola.queue.clear()
        for elemento in lista:
            cola.put(elemento)
        
        print("🔀 Cola después de mezclar:", list(cola.queue))
        print("✅ Mezcla realizada correctamente :D")

def destruir():
    cola.queue.clear()
    print("💥 La cola fue vaciada completamente")

print("Bienvenido, este es un programa que te permite realizar diferentes operaciones con colas 😜")
while True:
    print(" ---- MENÚ COLA ---- ")
    print("1. Ver si está vacía")
    print("2. Agregar elemento")
    print("3. Eliminar elemento")
    print("4. Mostrar frente")
    print("5. Mostrar final")
    print("6. Mostrar datos")
    print("7. Contar elementos")
    print("8. Número mayor")
    print("9. Copiar cola")
    print("10. Mezclar cola")
    print("11. Vaciar cola")
    print("12. Salir")

    opcion = input("👉 Elige una opción: ")

    if opcion == "1":
        esta_vacia()
    elif opcion == "2":
        agregar()
    elif opcion == "3":
        eliminar()
    elif opcion == "4":
        mostrar_frente()
    elif opcion == "5":
        mostrar_final()
    elif opcion == "6":
        mostrar_datos()
    elif opcion == "7":
        contar()
    elif opcion == "8":
        mayor()
    elif opcion == "9":
        copiar()
    elif opcion == "10":
        mezclar()
    elif opcion == "11":
        destruir()
    elif opcion == "12":
        print("👋 Gracias por usar el programa")
        break
    else:
        print("❌ Opción inválida")
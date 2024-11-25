from operaciones import sumar, restar, multiplicar, dividir

def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    opcion = input("Elige una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == "1":
        a = input("Introduce el primer valor: ")
        b = input("Introduce el segundo valor: ")
        try:
            a = float(a)
            b = float(b)
            resultado = sumar(a, b)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Ambos valores deben ser int o float")
    elif opcion == "2":
        a = input("Introduce el primer valor: ")
        b = input("Introduce el segundo valor: ")
        try:
            a = float(a)
            b = float(b)
            resultado = restar(a, b)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Ambos valores deben ser int o float")
    elif opcion == "3":
        a = input("Introduce el primer valor: ")
        b = input("Introduce el segundo valor: ")
        try:
            a = float(a)
            b = float(b)
            resultado = multiplicar(a, b)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Ambos valores deben ser int o float")
    elif opcion == "4":
        a = input("Introduce el primer valor: ")
        b = input("Introduce el segundo valor: ")
        try:
            a = float(a)
            b = float(b)
            resultado = dividir(a, b)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Ambos valores deben ser int o float")
    elif opcion == "5":
        print("Saliendo...")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        ejecutar_opcion(opcion)
        if opcion == "5":
            break





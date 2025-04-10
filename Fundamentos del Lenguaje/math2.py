import mates

numero1 = 9
numero2 = 2

while True:
    print(f"Los números son: {numero1} y {numero2}")
    print("Seleccione una opción:")
    print("1. Dividir")
    print("2. Multiplicar")
    print("3. Restar")
    print("4. Sumar")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
            print(mates.div(numero1, numero2))
    elif opcion == '2':
            print(mates.mult(numero1, numero2))
    elif opcion == '3':
            print(mates.rest(numero1, numero2))
    elif opcion == '4':
            print(mates.sum(numero1, numero2))
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
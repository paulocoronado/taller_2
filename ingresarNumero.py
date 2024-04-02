def ingresar_numero_entero():
    # Solicitar al usuario que ingrese un número entero
    numero_entero = input("Por favor, ingresa un número entero positivo mayor que cero: ")

    # Intentar convertir la entrada del usuario a un número entero
    try:
        numero_entero = int(numero_entero)
        # Verificar si el número es mayor que cero
        if numero_entero > 0:
            return numero_entero
        else:
            print("Error: Debes ingresar un número entero positivo mayor que cero.")
            return ingresar_numero_entero()
    except ValueError:
        # Si la entrada no es un número entero válido, mostrar un mensaje de error y volver a solicitar
        print("Error: Debes ingresar un número entero válido.")
        return ingresar_numero_entero()

def imprimir_primos(numero):
    # Iterar sobre el rango desde 2 hasta numero*100
    for num in range(2, numero * 100 + 1):
        # Verificar si el número es primo
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)

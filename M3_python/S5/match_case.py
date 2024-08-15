# match case

while True: #mientras sea verdadero
    opcion = input('Hola bienvenido\n'
                + 'Seleccione una opción\n'
                + '1.- Opcion 1\n'
                + '2.- Opcion 2\n'
                + '3.- Opcion 3\n'
                + '4.- Salir\n'
                )


    match opcion: # cada caso se valida con el valor de la variable
        case '1':
            print('opcion 1')
        case '2':
            print('opcion 2')
        case '3':
            print('opcion 3')
        case '4':
            print('Hasta luego....')
            break
        case _:
            print('Opción no valida, ingrese otra opción')          
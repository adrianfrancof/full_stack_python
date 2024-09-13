def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            datos = file.readlines()
            print(datos)
            for i in datos:
                print(i.strip())
    except FileNotFoundError:
        print('Error: Archivo no existe')
        
leer_archivo('informacion.dat') 
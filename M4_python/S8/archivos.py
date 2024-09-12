'''
'r': Por defecto, para leer el fichero.
'w': Para escribir en el fichero.
'x': Para la creación, fallando si ya existe.
'a': Para añadir contenido a un fichero existente.
'b': Para abrir en modo binario.
'rb': Para leer archivo en modo binario.
'wb': Para escribir en archivo en modo binario.

algunas funciones para files
open()
close()
write()
writelines()
read()
readline()
readlines()
'''
# lectura de archivos, 'r': Por defecto, para leer el fichero.
def read_file():
    try:
        with open('nombre_archivo.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Archivo no encontrado.")
        
# escritura en fichero, 'w': Para escribir en el fichero.
def write_file():
    with open('nombre_archivo.csv', 'w') as file:
        file.write("Esta es una nueva linea.")

# solo creación del archivo, 'x': Para la creación, fallando si ya existe. raises FileExistsError
def create_file_exclusive():
    try:
        with open('nombre_archivo.txt', 'x') as file:
            file.write("Esta archivo es solo creado.")
    except FileExistsError:
        print("Archivo ya existente.")

# agregar contenido a archivo existente, si el archivo no existe lo crea
# 'a': Para añadir contenido a un fichero existente.        
def append_file():
    with open('nombre_archivo.txt', 'a') as file:
        file.write("Esta linea se agrega al archivo.")

# escritura y lectura de archivos binarios        
def write_binary_file():
    with open('nombre_archivo.bin', 'wb') as file:
        file.write(b' binary data.')

def read_binary_file():
    try:
        with open('nombre_archivo.bin', 'rb') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Archivo binario no encontrado.")        


#carga de archivo, lectura y creacion si el archivo no existe
def load_file():
    try:
        with open('nombre_archivo.csv','r') as file:#apertura y cierra el archivo, se puede establecer el tipo de apertura, r es para leer
            datos = file.readlines() #retorna una lista de tipo str con todas las lineas existentes
    except FileNotFoundError: #si ocurre el error de archivo no existe, se procede a crearlo
        datos = []
        with open('nombre_archivo.csv','w') as file:
            file.writelines(datos) #crear el archivo si no existe, w es para escribir
    return datos

#crear solo el arhivo
def create_file():
    datos = []
    with open('nombre_archivo.txt','w') as file:
            file.writelines(datos) #crear el archivo si no existe, w es para escribir
    
#crear solo el arhivo y no cerrarlo automaticamente
def create_file():
    try:
        file = open('nombre_archivo.txt','w') #se crea el arhivo
        file.close() #se cierra el archivo
    except FileExistsError:
        print("Archivo ya existe")
    finally:
        file.close() #se cierra el archivo    
       
#guardado o escribiendo un dato dentro del archivo
def save_file():
    with open('nombre_archivo.txt','w') as file:
        dato = "dato a escribir"
        file.write(str(dato)) #se va escribiendo en el archivo

#guardado o escribiendo un dato dentro del archivo
def write_in_file():
    try:
        file = open('nombre_archivo.txt','w')
        file.write("dato a escribir") #se va escribiendo en el archivo
    except FileNotFoundError:
        print("Archivo no existe")
    finally: file.close() #se cierra el archivo
    
# load_file()
write_file()
# read_file()
# append_file()
# read_file()
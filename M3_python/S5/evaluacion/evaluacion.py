'''
Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, 
e imprimir en pantalla las consonantes restantes y su posición dentro de dicha palabra.
'''
#        [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
#        [p a r a l e l e p í p  e  d  o]
palabra = 'paralelepípedo'

patron = 'aeiouAEIOUáéíóúÁÉÍÓÚ' # patron a cumplir

acumulador_consonantes = '' # se inicializa vacia

for i in range(len(palabra)): # i es el indice de cada caracter
    if palabra[i] not in patron: # if caracter not in patron # palabra[i] retorna cada elemento del indice
        acumulador_consonantes += palabra[i] # se acumula cada caracter consonante dentro de una variable
        print(f'La letra {palabra[i]} se encuentra en la posicion {i}')
        
print(f'Las letras consonantes son {acumulador_consonantes}')
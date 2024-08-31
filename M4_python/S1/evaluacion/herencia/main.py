from modelo.Futbolista import Futbolista
from modelo.Entrenador import Entrenador

futbolista_uno = Futbolista(1, 'Arturo', 'Vidal', 37, 15, 'mediocampista')
futbolista_dos = Futbolista(2, 'Zinedine', 'Zidane', 45, 10, 'mediocampista')


entrenador_uno = Entrenador(1, 'Carlo', 'Ancelotti', 68, 'f001')


futbolista_uno.concentrarse()
futbolista_uno.jugar_partido()

entrenador_uno.viajar()

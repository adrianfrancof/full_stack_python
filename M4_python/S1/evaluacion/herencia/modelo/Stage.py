class Stage:
    def __init__(self, futbolista, entrenador):
        self.futbolista = futbolista
        self.entrenador = entrenador
        
    def __str__(self) -> str:
        return f'Stage(futbolista{self.futbolista})'            
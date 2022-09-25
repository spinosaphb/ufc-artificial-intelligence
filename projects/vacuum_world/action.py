

class Action:

    def __init__(self, name: str | bool) -> None:
        if isinstance(name, bool):
            self._name = name and 'Esquerda' or 'Direita'
        else:
            self._name = name
 
    @property
    def name(self) -> str:
        return self._name 

    def __str__(self) -> str:
        return self.name
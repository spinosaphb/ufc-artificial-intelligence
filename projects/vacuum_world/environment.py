
from action import Action


class Environment:

    def __init__(self, is_dirty_a: bool, is_dirty_b: bool, agent_location: bool) -> None:

        self._is_dirty = {
            'a': is_dirty_a,
            'b': is_dirty_b
        }
        self._agent_location = True if agent_location == 'A' else False

    @property
    def is_dirty_a(self) -> bool:
        return self._is_dirty["a"]

    @is_dirty_a.setter
    def is_dirty_a(self, __obj: bool):
        if not isinstance(__obj, bool):
            raise TypeError
        
        self._is_dirty['a'] = __obj

    @property
    def is_dirty_b(self) -> bool:
        return self._is_dirty["b"]

    @is_dirty_b.setter
    def is_dirty_b(self, __obj: bool):
        if not isinstance(__obj, bool):
            raise TypeError
        
        self._is_dirty['b'] = __obj

    @property
    def agent_location(self) -> bool:
        return self._agent_location

    @agent_location.setter
    def agent_location(self, __obj: bool):
        if not isinstance(__obj, bool):
            raise TypeError
        self._agent_location = __obj


    def update(self, action: Action):
        match(action.name):
            case 'Aspirar':
                if self.agent_location:
                    self.is_dirty_a = False
                else:
                    self.is_dirty_b = False

            case 'Direita':
                self.agent_location = False
            
            case 'Esquerda':
                self.agent_location = True


    def __str__(self) -> str:
        return str(self.getattrs())


    def getattrs(self) -> dict:
        return {
            'agent_location': getattr(self, 'agent_location') and 'A' or 'B',
            'is_dirty_a': getattr(self,'is_dirty_a'),
            'is_dirty_b': getattr(self,'is_dirty_b')
        }
from dataclasses import dataclass
from typing import Optional
from .graph import State

@dataclass
class Node:
    state: State
    cost: int = 0
    dad: 'Node' = None

    def __eq__(self, __o) -> bool:
        if isinstance(__o, State):
            return __o == self.state
        elif isinstance(__o, Node):
            return __o.state == self.state
        else: raise TypeError()

    def __le__(self, __o: 'Node') -> bool:
        if not isinstance(__o, Node):
           raise TypeError()
        return self.cost <= __o.cost

    def __lt__(self, __o: 'Node') -> bool:
        if not isinstance(__o, Node):
           raise TypeError()
        return self.cost < __o.cost 

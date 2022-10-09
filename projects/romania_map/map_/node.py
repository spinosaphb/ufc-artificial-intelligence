from ctypes import Union
from dataclasses import dataclass
from typing import Optional
from .graph import State

@dataclass
class Node:
    state: State
    cost: Optional[int] 
    dad: Optional['Node']

    def __eq__(self, __o) -> bool:
        if isinstance(__o, State):
            return __o == self.state
        elif isinstance(__o, Node):
            return __o.state == self.state
        else: raise TypeError()

    @classmethod
    def state2node(cls, state: State) -> 'Node':
        if not isinstance(state, State):
            raise TypeError(f"Type {type(state)} is not valid")
        return Node(state, 0, None)
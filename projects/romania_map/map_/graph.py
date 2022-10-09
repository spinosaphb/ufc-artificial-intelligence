
from dataclasses import dataclass
from itertools import starmap
from typing import Any, Dict, List, Optional
"""
Module for classes of graph
"""

class Graph:
    
    def __init__(self, map_: List['State']) -> None:
        self._map: Dict[str, 'State'] = {state.city: state for state in map_}

    def __getitem__(self, state: Any):
        if isinstance(state, str):
            return self._map[state]
        elif isinstance(state, State):
            return self._map[state.city]
        else:
            raise TypeError(f"Type {type(state)} not is a valid")
    
    @classmethod
    def dict2graph(cls, map_: Dict[str, dict]) -> 'Graph':
        map_ = [
            State(state, [*starmap(Transiction, adjs.items())])
            for state, adjs in map_.items()
        ]
        return Graph(map_)

    def __str__(self) -> str:
        return  str(self._map)

    
@dataclass
class State:
    city: str
    adjs: List['Transiction']

    def __eq__(self, __o: 'State') -> bool:
        return __o == self.city

@dataclass
class Transiction:
    state: str
    cost: int 

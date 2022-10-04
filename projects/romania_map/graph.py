
from dataclasses import dataclass
from itertools import starmap
from typing import Dict, List
"""
Module for classes of graph
"""


class Graph:
    
    def __init__(self, map_: List['State']) -> None:
        self._map = map_

    @classmethod
    def dict2graph(self, map_: Dict[str, dict]) -> 'Graph':
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

@dataclass
class Transiction:
    target: State
    cost: int 

    

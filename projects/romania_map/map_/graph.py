
from dataclasses import dataclass
from itertools import starmap
from typing import Dict, List, Optional
"""
Module for classes of graph
"""

class Graph:
    
    def __init__(self, map_: List['State']) -> None:
        self._map: Dict[str, 'State'] = {state.city: state for state in map_}

    def __getitem__(self, state_name: str):
        return self._map[state_name]

    @classmethod
    def dict2graph(cls, map_: Dict[str, dict]) -> 'Graph':
        map_ = [
            State(state, [*starmap(Transiction, adjs.items())])
            for state, adjs in map_.items()
        ]
        return Graph(map_)   


    def graph2tree(self) -> dict:
        map_ = {}
            
        for state in self._map.values():
            node = Node(state.city, 0, None, None)
            node.childs =[*map(lambda adj: Node(
                adj.target,
                adj.cost,
                node,
                None
            ), state.adjs)]
            map_.update({state.city: node})

        return map_


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
    target: str
    cost: int 


@dataclass
class Node:
    value: State
    cost: Optional[int] 
    dad: Optional['Node'] 
    childs: Optional[List['Node']] 

    def __eq__(self, __o: 'Node') -> bool:
        return __o == self.value
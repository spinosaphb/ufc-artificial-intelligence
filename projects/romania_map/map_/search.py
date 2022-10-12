from dataclasses import dataclass
from typing import Callable, List
from .graph import State, Graph, Transiction
from .node import Node
from .pqueue import PriorityQueue

def _backtrack_path(node: Node) -> None:
    if node.dad is None:
        return
    _backtrack_path(node.dad)
    print(node.state.city, node.cost)


def _trn2node(graph: Graph, dad: Node = None) -> Callable[[Transiction], Node]:
    return lambda trn: Node(
        state=graph[trn.state_name],
        cost=trn.cost+(dad and dad.cost or 0),
        dad=dad
    )
    

def childs(node: Node, graph: Graph):
    return map(_trn2node(graph, node), node.state.adjs)

def bfs(graph: Graph, origin: State, target: State) -> bool:
    """
    Breath-first search
    ---
    """
    edge: List[Node] = [Node(origin)]
    explored: List[Node] = []
    
    while True:
        if len(edge) == 0: return False
        node = edge.pop(0)
        explored.append(node)
        for child in childs(node, graph):
            if child not in [*explored, *edge]:
                if child.state == target.city:
                    _backtrack_path(child)
                    return True
                edge.append(child)

def ucs(graph: Graph, origin: State, target: State) -> bool:
    """
    Uniform-cost search
    ---
    """
    edge: PriorityQueue = PriorityQueue(Node(origin))
    explored: List[Node] = []

    while True:
        if len(edge) == 0: return False
        node: Node = edge.pop()
        if node.state == target.city:
            _backtrack_path(node)
            return True
        explored.append(node)
        for child in childs(node, graph):
            if child not in [*explored, *edge]:
                edge.put(child)
            elif child in edge:
                edge.put(min(edge[child], child)) 

def dfs(graph: Graph, origin: State, target: State) -> bool:
    """
    Deep-first Search 
    """
    edge: List['Node'] = [Node(origin)]
    explored: List[Node] = []
    
    while True:
        if len(edge) == 0: return False
        node: Node = edge.pop()
        explored.append(node)
        for child in childs(node, graph):
            if child not in [*explored, *edge]:
                if child.state == target.city:
                    _backtrack_path(child)
                    return True
                edge.append(child)

@dataclass
class Searcher:

    graph: Graph
    origin: State = None
    target: State = None

    def _set_origin_target(self, origin: State, target: State) -> tuple[State, State]:
        origin = origin or self.origin
        target = target or self.target
        return origin, target

    def search(self, how: str, origin: State = None, target: State = None):
        origin, target = self._set_origin_target(origin, target) 
        return getattr(self, how)(origin, target)

    def breath(self, origin: State = None, target: State = None):
        origin, target = self._set_origin_target(origin, target) 
        return bfs(self.graph, origin, target)
    
    def uniform(self, origin: State = None, target: State = None):
        origin, target = self._set_origin_target(origin, target) 
        return ucs(self.graph, origin, target)
    
    def deep(self, origin: State = None, target: State = None):
        origin, target = self._set_origin_target(origin, target) 
        return dfs(self.graph, origin, target) 
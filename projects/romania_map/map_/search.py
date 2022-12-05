from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List, TypeVar
from .graph import State, Graph, Transiction
from .node import Node
from .pqueue import PriorityQueue

from config import load_path
load_path()
from utils import show_line
from tools import infinity

_T = TypeVar("_T")

def _backtrack_path(node: Node) -> List[Dict[str, Any]]:
    if node.dad is None:
        return [(node.state.city, node.cost)]
    return [*_backtrack_path(node.dad), (node.state.city, node.cost)]


def _trn2node(graph: Graph, dad: Node = None) -> Callable[[Transiction], Node]:
    return lambda trn: Node(
        state=graph[trn.state_name],
        cost=trn.cost+(dad and dad.cost or 0),
        dad=dad
    )

def _childs(node: Node, graph: Graph):
    return map(_trn2node(graph, node), node.state.adjs)

def _make_heuristic_fn(cost_map: Dict[str, int]) -> Callable[[Node], int]:
    return lambda node: cost_map[node.state.city] 

def _make_cost_fn() -> Callable[[Node], int]:
    return lambda node: node.cost

def _show_info_search(edge: Iterable, explored: Iterable, i: int):
    show_line(
        f"Edge rest: {len(edge)} | Explored: {len(explored)} | Iter: {i}", clear=False)

def _notin(ite: Iterable) -> Callable[[_T], bool]:
    return lambda elem: elem not in ite


def normal_search(graph: Graph, origin: State, target: State, popidx) -> bool:
    """
    Breath-first and Deep-first search
    ---
    """
    edge: List[Node] = [Node(origin)]
    explored: List[Node] = []
    
    for i in infinity():
        if len(edge) == 0: return False
        node = edge.pop(popidx)
        explored.append(node)
        for child in filter(_notin([*explored, *edge]), _childs(node, graph)):
            if child.state == target.city:
                path = _backtrack_path(child) 
                from pprint import pprint
                pprint(path)
                return path
            edge.append(child)

def priority_search(
    graph: Graph,
    origin: State,
    target: State,
    fn: Callable[[Node], int] = None) -> bool:
    """
    Uniform-cost, Greedy, A* search
    ---
    """
    edge: PriorityQueue = PriorityQueue([Node(origin)], fn)
    explored: List[Node] = []
    for i in infinity():
        if len(edge) == 0: return False
        node: Node = edge.pop()
        if node.state == target.city:
            path = _backtrack_path(node) 
            from pprint import pprint
            pprint(path)
            return path
        explored.append(node)
        for child in _childs(node, graph):
            if child not in [*explored, *edge]:
                edge.put(child)
            elif child in edge:
                edge.put(min(edge[child], child)) 


def ucs(graph: Graph, origin: State, target: State):
    """
    Uniform-cost search
    ---
    """
    return priority_search(graph, origin, target)

def bfs(graph: Graph, origin: State, target: State):
    """
    Breath-first Search 
    """
    return normal_search(graph, origin, target, 0)

def dfs(graph: Graph, origin: State, target: State) -> bool:
    """
    Deep-first Search 
    """
    return normal_search(graph, origin, target, -1)

def greedy_search(
    graph: Graph,
    origin: State,
    target: State,
    cost_map_: dict[str, int]) -> bool:
    """
    Greedy Search
    """
    h_fn = _make_heuristic_fn(cost_map_)

    return priority_search(graph, origin, target, h_fn)

def astar_search(
    graph: Graph,
    origin: State,
    target: State,
    cost_map_: dict[str, int]) -> bool:

    h_fn = _make_heuristic_fn(cost_map_)
    g_fn = _make_cost_fn()
    
    return priority_search(graph, origin, target, lambda n: h_fn(n) + g_fn(n))   


@dataclass
class Searcher:

    graph: Graph
    origin: State = None
    target: State = None
    h_map: Dict = None

    def _set_attrs(self, origin: State, target: State, h_map = None) -> tuple[State, State]:
        origin = origin or self.origin
        target = target or self.target
        h_map = h_map or self.h_map
        return origin, target, h_map

    def search(self, how: str, origin: State = None, target: State = None):
        origin, target, _ = self._set_attrs(origin, target) 
        return getattr(self, how)(origin, target)

    def breath(self, origin: State = None, target: State = None):
        origin, target, _ = self._set_attrs(origin, target) 
        return bfs(self.graph, origin, target)
    
    def uniform(self, origin: State = None, target: State = None):
        origin, target, _ = self._set_attrs(origin, target) 
        return ucs(self.graph, origin, target)
    
    def deep(self, origin: State = None, target: State = None):
        origin, target, _ = self._set_attrs(origin, target) 
        return dfs(self.graph, origin, target) 

    def greedy(self, origin: State = None, target: State = None, cost_map = None):
        origin, target, h_map = self._set_attrs(origin, target, cost_map) 
        return greedy_search(self.graph, origin, target, h_map)

    def astar(self, origin: State = None, target: State = None, cost_map = None):
        origin, target, h_map = self._set_attrs(origin, target, cost_map) 
        return astar_search(self.graph, origin, target, h_map)
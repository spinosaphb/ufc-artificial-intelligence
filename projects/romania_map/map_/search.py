from pprint import pprint
from typing import List
from .graph import State, Graph
from .node import Node
from .pqueue import PriorityQueue

def backtrack_path(node: Node) -> None:
    if node.dad is None:
        return
    backtrack_path(node.dad)
    print(node.state.city, node.cost)


def bfs(graph: Graph, origin: State, target: State) -> bool:
    """
    Breath-firsth search
    ---
    """
    edge: List[Node] = [Node.state2node(origin)]
    explored: List[Node] = []
    
    while(True):
        if len(edge) == 0: return False
        node = edge.pop(0)
        explored.append(node)

        for adj in node.state.adjs:
            child = Node(graph[adj.state], adj.cost + node.cost, node)
            if child not in [*explored, *edge]:
                if child.state == target.city:
                    backtrack_path(child)
                    return True
                edge.append(child)

def ucs(graph: Graph, origin: State, target: State) -> bool:
    """
    Uniform-firsth search
    ---
    """
    edge: PriorityQueue = PriorityQueue()
    edge.put(Node.state2node(origin))
    explored: List[Node] = []
    
    while(True):
        if len(edge) == 0: return False
        node: Node = edge.pop()
        if node.state == target.city:
            backtrack_path(node)
            return True
        explored.append(node)
        for adj in node.state.adjs:
            child = Node(graph[adj.state], adj.cost + node.cost, node)
            if child not in [*explored, *edge]:
                edge.put(child)
            elif child in edge:
                edge.put(min(edge[child], child)) 



from typing import Dict, List
from .graph import Node

def bfs(tree: Dict[str, Node], start: Node, target: Node):
    edge: List[Node] = [start]
    explored: List[Node] = []

    def backtrack_path(node: Node) -> None:
        if node.dad is None:
            return node.cost
        cost = node.cost + backtrack_path(node.dad)
        print(node.value, cost)
        return cost

    while(True):
        if len(edge) == 0: return False
        node = edge.pop(0)
        node.childs = tree[node.value].childs
        explored.append(node)

        for child in node.childs:
            child.dad = node
            if child not in [*explored, *edge]:
                if child.value == target.value:
                    backtrack_path(child)
                    return True
                edge.append(child)
        



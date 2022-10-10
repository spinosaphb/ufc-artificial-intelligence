import json
from map_ import Graph
from map_.search import bfs, ucs
from config import MAP_PATH
import sys
from core import flow, format_name
from utils import show_line

if __name__ == "__main__":
    with open(MAP_PATH, 'r') as file:
        map_: dict = json.load(file)
    
    graph = Graph.dict2graph(map_)

    origin, target = None, None

    def format_name_(*args, **kwargs): return format_name(map_, *args, **kwargs)
    def flow_(*args, **kwargs): return flow(map_, *args, **kwargs)

    match len(sys.argv):
        case 1:
            print(graph)
            origin, target = flow_()
        case 2:
            origin = format_name_(sys.argv[1])
            _, target = flow_(get_origin=False)
        case 3:
            origin, target = map(format_name_, sys.argv[1:])
        case _:
            raise RuntimeError("Many arguments!")
    
    show_line("Breadth-first search", clear=False)
    bfs(graph, graph[origin], graph[target])
    show_line("Uniform-cost search", clear=False)
    ucs(graph, graph[origin], graph[target])
    show_line("", clear=False)

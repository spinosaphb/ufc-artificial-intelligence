import json
from map_ import Graph, bfs
from config import load_path, MAP_PATH
load_path()
from utils import show_line
from pprint import pprint

if __name__ == "__main__":

    with open(MAP_PATH, 'r') as file:
        map_ = json.load(file)
    
    graph = Graph.dict2graph(map_)
    
    print(graph)
    
    def show_map():
        dashes = show_line("Romenia Map")
        pprint(map_)
        print(dashes)
    show_map()

    def get_data():
        global origin, target
        origin = input("origin: ").capitalize()    
        target = input("target: ").capitalize()
    get_data()
    
    while not((origin in map_) and (target in map_)):
        show_map()
        print("Origin or Target does not in map!\n")
        get_data()
    show_line('Path', False)
    bfs(graph, graph[origin], graph[target])


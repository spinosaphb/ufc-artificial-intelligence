import json
from graph import Graph

if __name__ == "__main__":
    with open('map.json', 'r') as file:
        map_ = json.load(file)
    
    graph = Graph.dict2graph(map_)
    print(graph)
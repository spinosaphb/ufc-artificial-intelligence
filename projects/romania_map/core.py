from typing import Tuple
from config import load_path, DEFAULT_TARGET, DEFAULT_ORIGIN
load_path()
from utils import show_line
from pprint import pprint


def format_name(map_: dict, city_name: str, default: str = None):
    city_name = city_name.capitalize() or default
    if city_name not in map_:
        raise IndexError("City not in Graph!")
    return city_name

def get_city(map_: dict, how : str):
    """
    ### Parameters:
    map_: graph
    how: origin or target
    """

    DEFAULT = DEFAULT_TARGET if how == "target" \
        else DEFAULT_ORIGIN if how == "origin" \
        else None

    if DEFAULT is None: raise RuntimeError("how must be 'origin' or 'target'")
    
    while(True):
        try:
            city = format_name(map_, input(f"origin[{DEFAULT}]: "), DEFAULT) 
            break
        except IndexError as e:
            print(e)
            continue
    print(city)
    return city

def flow(map_: dict, get_origin = True) -> Tuple[str, str]:
    """
    If Anyone arg was passed
    
    Return:
    ---
    The origin and target
    """ 
    
    def show_map():
        dashes = show_line("Romenia Map")
        pprint(map_)
        print(dashes)
    show_map()

    def get_data():
        states = []

        if get_origin:
            states.append(get_city(map_, "origin"))
        else: states.append(DEFAULT_ORIGIN)
        
        states.append(get_city(map_, "target"))
        
        return states
        

    origin, target = get_data()
    
    while not((origin in map_) and (target in map_)):
        show_map()
        if get_origin:
            print("Origin or Target does not in map!\n")
        else:
            print("Target does not in map!\n")
        origin, target = get_data()
    show_line('Path', False)

    return origin, target

import os, sys
def load_path():
    abs_path = os.path.abspath(os.curdir)
    project_dir = os.path.dirname(abs_path)
    sys.path.append(project_dir)

MAP_PATH = "romenia.json"
COST_MAP_PATH = "cost_map_romenia.json"

DEFAULT_ORIGIN = "Arad"
DEFAULT_TARGET = "Bucharest"
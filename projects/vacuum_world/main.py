import os
from environment import Environment
from agent import Agent
from world import VacuumWorld

from utils import str2agent, str2bool, env_data

if __name__ == "__main__":

    print("\033c")
    
    cols, _ = os.get_terminal_size()

    data = env_data.copy()

    project_name = "Vacuum World"
    words_size = len(project_name)
    n_dash = (cols - words_size)//2
    dashes = n_dash*'-'
    
    print(f"{dashes + project_name + dashes}")
    
    for att, params in data.items():
        prompt, value = params.values()
        
        if 'dirty' in att:
            data[att] = str2bool(input(prompt) or value)  
        else:
            data[att] = str2agent(input(prompt) or value) 

    env = Environment(**data)
    
    VacuumWorld(env, Agent()).start(input('steps [10]/?: ') or 10, 'True')

    

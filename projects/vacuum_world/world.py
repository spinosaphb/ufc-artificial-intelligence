from environment import Environment
from agent import Agent

from pprint import pprint


class VacuumWorld:
    
    def __init__(self, env: Environment, agent: Agent) -> None:
        self.env = env
        self.agent = agent

    def start(self, steps: int, show_steps: bool = True) -> None:
        
        for i in range(steps):
            print('Env state:')
            pprint(self.env.getattrs())

            perception = self.agent.perceives(self.env)
            action = self.agent.act(perception)
            self.env.update(action)

            if show_steps:
                print(f'step: {i}, action: {action}')

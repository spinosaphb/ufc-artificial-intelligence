

from environment import Environment
from perception import Perception
from action import Action


class Agent:
    
    def __init__(self) -> None:
        pass

    def perceives(self, env: Environment) -> Perception:
        location = env.agent_location
        is_dirty = env.is_dirty_a if location else env.is_dirty_b
        return Perception(location, is_dirty)

    def act(self, per: Perception) -> Action:
        match(per.is_dirty):
            case True:
                return Action('Aspirar')
            case False:
                return Action(not per.location)
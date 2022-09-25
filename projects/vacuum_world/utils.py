import re

def str2bool(word: str) -> bool:
    if re.match(r'f.*', word.lower()):
        return False
    if re.match(r't.*', word.lower()):
        return True
    raise ValueError(f"Invalid value for dirty, provided: {word}")


def str2agent(word: str) -> str:
    if word.lower() == 'a':
        return "A"
    if word.lower() == 'b':
        return "B"
    raise ValueError(f"Invalid value for agent, provided: {word}")

env_data = {
    'is_dirty_a': {
        'prom': 'A is Dirty ([true]/false)? ',
        'value': 'True'
    },
    'is_dirty_b': {
        'prom': 'B is Dirty ([true]/false)? ',
        'value': 'True'
    },
    'agent_location': {
        'prom': 'Agent location ([A]/B): ',
        'value': 'A'
    }
}
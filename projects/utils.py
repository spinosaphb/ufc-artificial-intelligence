import os

def show_line(project_name: str, clear=True) -> str:
    if clear: print("\033c")
    
    cols, _ = os.get_terminal_size()
    project_name = project_name
    words_size = len(project_name)
    n_dash = (cols - words_size)//2
    dashes = n_dash*'-'

    print(f"{dashes + project_name + dashes}")
    
    return len(project_name)*'-'+2*dashes
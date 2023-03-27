from coffeeMachine import coffeeMachine
from utils import clear_terminal

def launch():
    
    machine = coffeeMachine()
    valid_machine = True 
    clear_terminal()

    while valid_machine:
        valid_machine = machine.options()

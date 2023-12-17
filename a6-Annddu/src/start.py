#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#
from ui import *
from functions import *

def main():
    """
    Main function
    """
    undo_stack = []
    list_contestant = generate_list_contestant(10)
    undo_stack.append(copy.deepcopy(list_contestant))
    print_menu()
    while True:
        command = ask_for_command()
        try:
            list_contestant = copy.deepcopy(command_direction(command, list_contestant, undo_stack))
        except StopIteration:
            print_exit()
            break
        
main()
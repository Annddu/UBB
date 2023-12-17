#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#

def print_menu():
    print("(A) Add the result of a new participant \nadd <P1 score> <P2 score> <P3 score>\ninsert <P1 score> <P2 score> <P3 score> at <position>\n")
    print("(B) Modify scores \nremove <position> \nremove <start position> to <end position> \nreplace <old score> <P1 | P2 | P3> with <new score>\n")
    print("(C) Display participants whose score has different properties \nlist \nlist sorted \nlist [ < | = | > ] <score>\n")
    print("(D) Establish the podium \ntop <number> \ntop <number> <P1 | P2 | P3> \nnremove [ < | = | > ] <score>\n")
    print("(E) Undo\n")
    print("(F) Exit\n")

def print_exit():
    print("Exiting...")

def ask_for_command() -> str: 
    command = input("Enter an command: ")
    return command

def wrong_command():
    print("Please enter a valid comand (type help to see comands)\n")
    
def wrong_score():
    print("The scores should be between 0 and 10\n")
    
def wrong_average_score():
    print("The average score should be between 0 and 10\n")

def wrong_len(n):
    print(f"Enter a position between 0 and {n - 1}\n")
    
def wrong_top(n):
    print(f"Enter a number between 1 and {n - 1}\n")
    
def wrong_order():
    print("Change the order of the numbers\n")
    
def error_value():
    print(f"VALUE ERROR: The contestants/score/average score should be NUMBERS\n")
    
def error_idex():
    print("INDEX ERROR: The command is not complete\n")
    
def print_contestant(contestant_index, P1, P2, P3, average):
    print(f"Contestant number {contestant_index}-> P1: {P1} P2: {P2} P3: {P3} average: {average}")
    
def empty():
    print("The stack is EMPTY")    

def space():
    print()
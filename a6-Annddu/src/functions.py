#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#

from ui import *

import random
import copy

#get values and generate the list
def get_scores(contestant: dict):
    """
    The function returns the scores of a contestant
    :contestant: the contestant from who are going to be extracted the values
    """
    P1 = contestant["P1"]
    P2 = contestant["P2"]
    P3 = contestant["P3"]
    return P1, P2, P3

def get_average(contestant: dict):
    """
    The function returns the averages score of a contestant
    :contestant: the contestant from who are going to be extracted the average score
    """
    average = contestant["average"]
    return average

def create_contestant(P1: int, P2: int, P3: int) -> dict:
    """
    Create a contestant with the 'random' generated scores
    :P1: the score for the first problem
    :P2: the score for the second problem
    :P3: the score for the third problem
    """
    contestant = {"P1": P1, "P2": P2, "P3": P3, "average": float(P1+P2+P3)/3}
    return contestant

def add_contestant_to_list(list_contestant: list, contestant: dict) -> list:
    """
    Adds a contestant to the list
    :list_contest: the list that is going to store the contestant
    :contestant: the contestant which is going to be added to the list
    """
    list_contestant.append(contestant)
    return list_contestant

def generate_list_contestant(n: int) -> list:
    """
    Generate a list of n contestants with 'random' scores
    :param n: the numbers of contestants numbers to be generated
    :return: the list containing the generated contestants scores
    """
    list_contestant = []
    for contestants in range(n):
        P1 = random.randint(0,10)
        P2 = random.randint(0,10)
        P3 = random.randint(0,10)
        contestant = create_contestant(P1, P2, P3)
        add_contestant_to_list(list_contestant, contestant)
    return list_contestant

#commands 
#(A)
def add(list_contestant: list, P1: int, P2: int, P3: int):
    """
    Adds a contestant to the end of the list 
    :list_contestant: the destination list
    :P1: first score of the contestant
    :P2: second score of the contestant
    :P3: third score of the contestant
    """
    contestant = create_contestant(P1, P2, P3)
    add_contestant_to_list(list_contestant, contestant)

def insert(list_contestant: list, P1: int, P2: int, P3: int, position: int):
    """
    Inserts a contestant at the 'position' in the list 
    :list_contestant: the destination list
    :P1: first score of the contestant
    :P2: second score of the contestant
    :P3: third score of the contestant
    :position: the index where the contestant is going to be added
    """
    contestant = create_contestant(P1, P2, P3)
    list_contestant.insert(position, contestant)

#(B)
def remove(list_contestant: list, position: int):
    """
    Removes the points of a contestant
    :list_contestant: the destination list
    :position: the index where the points are going to be removed
    """
    list_contestant[position]["P1"] = 0
    list_contestant[position]["P2"] = 0
    list_contestant[position]["P3"] = 0
    list_contestant[position]["average"] = 0

def remove_a_to_b(list_contestant: list, first: int, last: int):
    """
    Removes the points of contesttants from the interval [a, b]
    :list_contestant: the destination list
    :first: the first index from the interval
    :last: the last index from the interval
    """
    for index_contestant in range(first, last + 1):
        remove(list_contestant, index_contestant)

def replace(list_contestan: list, position: int, problem: str, new_score: int):
    """
    Replace the score of one of the porblems of some contestant with a new score
    :list_contestant: the destination list
    :position: the number of the contestant
    :prblem: first/second/third problem
    :new_score: the new score of the problem
    """
    list_contestan[position][problem] = new_score
    list_contestan[position]["average"] = float(list_contestan[position]["P1"] + list_contestan[position]["P2"] + list_contestan[position]["P3"])/3

#(C)
def list(list_contestant: list):
    """
    Prints the list of contestants
    :list_contestant: the list that is going to be printed
    """
    for contestant_index, contestant in enumerate(list_contestant):
        P1, P2, P3 = get_scores(contestant)
        average = get_average(contestant)
        print_contestant(contestant_index, P1, P2, P3, average)
    space()

def list_sorted(list_contestant: list):
    """
    Sort the list in function of the average scores
    :list_contestant: the list that is going to be sorted
    """
    list_contestant_sorted = sorted( list_contestant, key=lambda x: x["average"], reverse = True)
    for contestant_index, contestant in enumerate(list_contestant_sorted):
        P1, P2, P3 = get_scores(contestant)
        average = get_average(contestant)
        print_contestant(list_contestant.index(contestant), P1, P2, P3, average)
    space()

def list_score(list_contestant: list, symbol: str, score: int):
    """
    Display the conterstants with a >/</= score
    :list_contestant: the list that is going to be verifyed
    :symbol: the symbol for comparison
    :score: the score for comparing
    """
    if symbol == '<':
        for contestant_index, contestant in enumerate(list_contestant):
            if list_contestant[contestant_index]["average"] < score:
                P1, P2, P3 = get_scores(contestant)
                average = get_average(contestant)
                print_contestant(contestant_index, P1, P2, P3, average)
    elif symbol == '=':
        for contestant_index, contestant in enumerate(list_contestant):
            if list_contestant[contestant_index]["average"] == score:
                P1, P2, P3 = get_scores(contestant)
                average = get_average(contestant)
                print_contestant(contestant_index, P1, P2, P3, average)
    elif symbol == '>':
        for contestant_index, contestant in enumerate(list_contestant):
            if list_contestant[contestant_index]["average"] > score:
                P1, P2, P3 = get_scores(contestant)
                average = get_average(contestant)
                print_contestant(contestant_index, P1, P2, P3, average)
    space()

#(D)
def top(list_contestant: list, places: int):
    """
    Display the top 'places' 
    :list_contestant: the list for searching
    :places: the number of places
    """
    list_contestant_sorted = sorted( list_contestant, key=lambda x: x["average"], reverse = True)
    for contestant_index, contestant in enumerate(list_contestant_sorted):
        if contestant_index == places - 1:
            break
        P1, P2, P3 = get_scores(contestant)
        average = get_average(contestant)
        print_contestant(list_contestant.index(contestant), P1, P2, P3, average)
    space()

def top_problem(list_contestant: list, problem: str, places: int):
    """
    Display the 'places' participants who obtained the highest score for 'problem', sorted descending by that score
    :list_contestant: the list for searching
    :places: the number of places
    :proble: the problem
    """
    list_contestant_sorted = sorted( list_contestant, key=lambda x: x[problem], reverse = True)
    for contestant_index, contestant in enumerate(list_contestant_sorted):
        if contestant_index == places - 1:
            break
        P1, P2, P3 = get_scores(contestant)
        average = get_average(contestant)
        print_contestant(list_contestant.index(contestant), P1, P2, P3, average)
    space()
    
def remove_more(list_contestant: list, symbol: str, score: int):
    """
    Set the scores of participants having an average score </>/= 'score' to 0
    :list_contestant: the list for searching
    :symbol: the symbol for comparison
    :score: the score for comparing
    """
    if symbol == '<':
        for contestant_index, contestant in enumerate(list_contestant):
            if list_contestant[contestant_index]["average"] < score:
                remove(list_contestant, contestant_index)
    elif symbol == '=':
        for contestant_index, contestant in enumerate(list_contestant):
            if list_contestant[contestant_index]["average"] == score:
                 remove(list_contestant, contestant_index)
    elif symbol == '>':
        for contestant_index, contestant in enumerate(list_contestant):
            if list_contestant[contestant_index]["average"] > score:
                 remove(list_contestant, contestant_index)
    space()

#(E)     
def undo(list_contestant: list, undo_stack):
    """
    We can undo the changes made to the list
    :list_contestant: the list of cantetans for returning in case of empty stack
    :undo_stack: the stack that store every change
    """
    if len(undo_stack) > 1:
        undo_stack.pop()
        space()
        return copy.deepcopy(undo_stack[len(undo_stack) - 1])
    else:  
        empty()
        space()
        return copy.deepcopy(list_contestant)

#direction to comands
def command_direction(command: str, list_contestant: list, undo_stack: list):
    """
    Directs/correct the command to a function and also is keeping track of the stack for undo
    :command: the command entered by the user
    :list_contestant: the list for working to it
    :undo_stack: the stack for memorizing the steps
    """
    words = command.split()
    
    try:
        #(A) Add the result of a new participant
        if words[0] == 'add' and words[1].isdigit and words[2].isdigit and words[3].isdigit  and len(words) == 4:
            try:
                if 0 <= int(words[1]) <= 10 and 0 <= int(words[2]) <= 10 and 0 <= int(words[3]) <= 10:
                    add(list_contestant ,int(words[1]), int(words[2]), int(words[3]))
                    undo_stack.append(copy.deepcopy(list_contestant))
                else:
                    wrong_score()
            except ValueError:
                error_value()
            except IndexError:
                error_idex()
                
        elif words[0] == 'insert' and words[1].isdigit and words[2].isdigit and words[3].isdigit and words[4] == 'at' and words[5].isdigit and len(words) == 6:
            try:
                if not 0 <= int(words[5]) <= len(list_contestant) - 1:
                    wrong_len(len(list_contestant))
                elif 0 <= int(words[1]) <= 10 and 0 <= int(words[2]) <= 10 and 0 <= int(words[3]) <= 10:
                    insert(list_contestant ,int(words[1]), int(words[2]), int(words[3]), int(words[5]))
                    undo_stack.append(copy.deepcopy(list_contestant))
                else:
                    wrong_score()
            except ValueError:
                error_value()
            except IndexError:
                error_idex()
            
        #(B) Modify scores
        elif words[0] == 'remove' and words[1].isdigit and len(words) == 2:
            try:
                if not 0 <= int(words[1]) <= len(list_contestant) - 1:
                    wrong_len(len(list_contestant))
                else:
                    remove(list_contestant, int(words[1]))
                    undo_stack.append(copy.deepcopy(list_contestant))
            except ValueError:
                error_value(len(list_contestant))
            except IndexError:
                error_idex()
                
        elif words[0] == 'remove' and words[1].isdigit and words[2] == 'to' and words[3].isdigit  and len(words) == 4:
            try:
                if not (0 <= int(words[1]) <= len(list_contestant) - 1) or not (0 <= int(words[3]) <= len(list_contestant) - 1):
                    wrong_len(len(list_contestant))
                elif not int(words[1]) < int(words[3]):
                    wrong_order()
                else:
                    remove_a_to_b(list_contestant, int(words[1]), int(words[3]))
                    undo_stack.append(copy.deepcopy(list_contestant))
            except ValueError:
                error_value(len(list_contestant))
            except IndexError:
                error_idex()
            
        elif words[0] == 'replace' and words[1].isdigit and (words[2] == 'P1' or words[2] == 'P2' or words[2] == 'P3') and words[3] == 'with' and words[4].isdigit and len(words) == 5:
            try:
                if not (0 <= int(words[1]) <= len(list_contestant) - 1):
                    wrong_len(len(list_contestant))
                elif not 0 <= int(words[4]) <= 10:
                    wrong_score()
                else:
                    replace(list_contestant, int(words[1]), words[2], int(words[4]))
                    undo_stack.append(copy.deepcopy(list_contestant))
            except ValueError:
                error_value(len(list_contestant))
            except IndexError:
                error_idex()
            
        #(C) Display participants whose score has different properties
        elif words[0] == 'list' and len(words) == 1:
            list(list_contestant)
        
        elif words[0] == 'list' and words[1] == 'sorted' and len(words) == 2:                        
            list_sorted(list_contestant)
        
        elif words[0] == 'list' and (words[1] == '<' or words[1] == '=' or words[1] == '>') and words[2].isdigit and len(words) == 3:
            try:
                if not 0 <= int(words[2]) <= 10:
                    wrong_average_score()
                else:
                    list_score(list_contestant, words[1], int(words[2]))
            except ValueError:
                error_value()
            except IndexError:
                error_idex()
            
        #(D) Establish the podium
        elif words[0] == 'top' and words[1].isdigit and len(words) == 2:
            try:
                if int(words[1]) >= len(list_contestant):
                    wrong_top(len(list_contestant))
                else:
                    top(list_contestant, int(words[1]))
            except ValueError:
                error_value()
            except IndexError:
                error_idex()    
            
        elif words[0] == 'top' and words[1].isdigit and (words[2] == 'P1' or words[2] == 'P2' or words[2] == 'P3') and len(words) == 3:
            try:
                if int(words[1]) >= len(list_contestant):
                    wrong_top(len(list_contestant))
                else:
                    top_problem(list_contestant, words[2], int(words[1]))
            except ValueError:
                error_value()
            except IndexError:
                error_idex()
                
        elif words[0] == 'remove' and (words[1] == '<' or words[1] == '=' or words[1] == '>') and words[2].isdigit:
            try:
                if not 0 <= int(words[2]) <= 10:
                    wrong_average_score()
                else:
                    remove_more(list_contestant, words[1], int(words[2]))
                    undo_stack.append(copy.deepcopy(list_contestant))
            except ValueError:
                error_value()
            except IndexError:
                error_idex()
        
        #(E) Undo
        elif words[0] == 'undo' and len(words) == 1:
            list_contestant = copy.deepcopy(undo(list_contestant, undo_stack))
            
        #(F) Exit
        elif words[0] == 'exit' and len(words) == 1:
            raise StopIteration
        
        #(G) Help
        elif words[0] == 'help' and len(words) == 1:
            print_menu()
        
        else: 
            wrong_command()

    except IndexError:
        error_idex()
    except ValueError:
        error_value()
    return copy.deepcopy(list_contestant)

def test_functions():
    """	
    Test the functions using asertions
    """
    # Test add
    list_contestant = []
    add(list_contestant, 5, 6, 7)
    assert len(list_contestant) == 1
    assert list_contestant[0]["P1"] == 5
    assert list_contestant[0]["P2"] == 6
    assert list_contestant[0]["P3"] == 7

    # Test insert
    insert(list_contestant, 3, 4, 2, 0)
    assert len(list_contestant) == 2
    assert list_contestant[0]["P1"] == 3
    assert list_contestant[0]["P2"] == 4
    assert list_contestant[0]["P3"] == 2

    # Test remove
    remove(list_contestant, 0)
    assert len(list_contestant) == 2
    assert list_contestant[0]["P1"] == 0
    assert list_contestant[0]["P2"] == 0
    assert list_contestant[0]["P3"] == 0

    # Test remove_a_to_b
    add(list_contestant, 1, 2, 3)
    add(list_contestant, 4, 5, 6)
    add(list_contestant, 7, 8, 9)
    remove_a_to_b(list_contestant, 1, 2)
    assert len(list_contestant) == 5
    assert list_contestant[1]["P1"] == 0
    assert list_contestant[1]["P2"] == 0
    assert list_contestant[1]["P3"] == 0
    assert list_contestant[2]["P1"] == 0
    assert list_contestant[2]["P2"] == 0
    assert list_contestant[2]["P3"] == 0

    # Test replace
    add(list_contestant, 8, 8, 7)
    replace(list_contestant, 5, "P1", 10)
    assert len(list_contestant) == 6
    assert list_contestant[5]["P1"] == 10
    assert list_contestant[5]["average"] == float(10 + 8 + 7) / 3

    print("All tests passed!")

test_functions()

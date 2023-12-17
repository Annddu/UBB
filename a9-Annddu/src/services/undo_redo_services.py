from src.ui.errors import *

class FunctionCall:
    def __init__(self, name, *params: list):
        self.__name = name
        self.__params = params
        
    def call(self):
        return self.__name(*self.__params)
    
    def __call__(self, *args, **kwargs):
        return self.call()
    
class Operation:
    def __init__(self, undo_function: FunctionCall, redo_function: FunctionCall):
        self.__undo_function = undo_function
        self.__redo_function = redo_function
        
    def undo(self):
        return self.__undo_function()
        
    def redo(self):
        return self.__redo_function()
  
class CascadingOperation:
    def __init__(self, operations):
        self.__operations = operations

    def undo(self):
        for operation in self.__operations:
            operation.undo()

    def redo(self):
        for operation in self.__operations:
            operation.redo()
       
class UndoRedoService:
    def __init__(self):
        self.__undo = []
        self.__redo = []
        
    def recordOperation(self, operation: Operation):
        self.__undo.append(operation)
        
    def undo(self):
        if not self.__undo:
            raise UndoError("No more undos")
        o = self.__undo.pop()
        self.__redo.append(o)
        o.undo()

    def redo(self):
        if not self.__redo:
            raise RedoError("No more redos")
        o = self.__redo.pop()
        self.__undo.append(o)
        o.redo()
        
# if __name__ == "__main__":
#     def fun_undo(a,b,c):
#         return a+b+c
    
#     def fun_redo(a,b,c):
#         return a*b*c
    
#     fundo = FunctionCall(fun_undo, 1, 2, 3)
#     funredo = FunctionCall(fun_redo, 10, 20, 30)
#     o = Operation(fundo, funredo)
#     print(o.undo())
#     print(o.redo())
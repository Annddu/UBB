from src.domain.idobject import IdObject
from src.ui.errors import *

class RepoIterator:
    def __init__(self, data: list):
        self.__data = data
        self.__pos = -1
        
    def __next__(self):
        #return the next item we iterate over
        self.__pos += 1
        if self.__pos >= len(self.__data):
            raise StopIteration()
        return self.__data[self.__pos]
    
class MemoryRepository:
    def __init__(self):
        self.__data = {}
    
    def add(self, object: IdObject):
        if not isinstance(object, IdObject):
            raise TypeError("The given object is not an IdObject!")
        
        if object.id in self.__data:
            raise ValidationException("An object with that id already exists!")
        
        self.__data[object.id] = object
        
    def remove(self, _id: int) -> IdObject:
        if self.find(_id) is None:
            raise ValidationException("There is no object with the given id!")
        return self.__data.pop(_id)
    
    def update(self, object: IdObject):
        if not isinstance(object, IdObject):
            raise TypeError("The given object is not an IdObject!")
        
        if object.id not in self.__data:
            raise ValidationException("There is no object with the given id!")
        
        self.__data[object.id] = object
    
    def get_all(self) -> list:
        return list(self.__data.values())
    
    def find(self, _id: int) -> IdObject:
        return self.__data[_id] if _id in self.__data else None #self.__data.keys()
    
    def __iter__(self):
        return RepoIterator(list(self.__data.values()))
    
    def __getitem__(self, item):
        if item not in self.__data:
            return None
        return self.__data[item]
    
    def __len__(self):
        return len(self.__data)
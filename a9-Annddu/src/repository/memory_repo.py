import pickle
from datetime import date

from src.domain.idobject import IdObject
from src.domain.book import Book
from src.domain.client import Client
from src.domain.reantal import Rental
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
    
class MemoryRepository():
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
        return self.__data[_id] if _id in self.__data.keys() else None #self.__data.keys()
    
    def __iter__(self):
        return RepoIterator(list(self.__data.values()))
    
    def __getitem__(self, item):
        if item not in self.__data:
            return None
        return self.__data[item]
    
    def __len__(self):
        return len(self.__data)
    
class Pickle(MemoryRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.load_file()
        
    def save_file(self):
        with open(self.__filename, 'wb') as file:
            pickle.dump(self.get_all(), file)
    
    def load_file(self):
        try:
            with open(self.__filename, 'rb') as file:
                __data = {}
                __data = pickle.load(file)
                for each in __data:
                    self.add(each)
        except FileNotFoundError:
            pass
            
    def add(self, object: IdObject):
        MemoryRepository.add(self, object)
        self.save_file()
        
    def remove(self, _id: int) -> IdObject:
        object = MemoryRepository.remove(self, _id)
        self.save_file()
        return object
    
    def update(self, object: IdObject):
        MemoryRepository.update(self, object)
        self.save_file()
        
class TextRepository(MemoryRepository):
    def __init__(self, filename, book_repo = None, client_repo = None):
        super().__init__()
        self.__filename = filename
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.load_file()
    
    #####  
    def save_file(self):
        if self.__filename == "books.txt":
            self.File_object = open(self.__filename ,"w", encoding="utf-8")
            strings = ''
            for each in self.get_all():
                strings += f"{each.id},{each.title},{each.author} \n"
            self.File_object.write(strings)
            self.File_object.close()
        elif self.__filename == "clients.txt":
            self.File_object = open(self.__filename ,"w", encoding="utf-8")
            strings = ''
            for each in self.get_all():
                strings += f"{each.id},{each.name} \n"
            self.File_object.write(strings)
            self.File_object.close()
        elif self.__filename == "rentals.txt":
            self.File_object = open(self.__filename ,"w", encoding="utf-8")
            strings = ''
            for each in self.get_all():
                strings += f"{each.id},{each.book.id},{each.client.id},{each.rented_date},{each.returned_date} \n"
            self.File_object.write(strings)
            self.File_object.close()
    
    def load_file(self):
        try:
            with open(self.__filename, 'r', encoding="utf-8") as file:
                __data = {}
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue
                    object = line.split(',')
                    if self.__filename == "books.txt":
                        object = Book(int(object[0]), object[1], object[2])
                        self.add(object)
                    elif self.__filename == "clients.txt":
                        object = Client(int(object[0]), object[1])
                        self.add(object)
                    elif self.__filename == "rentals.txt":
                        object[3] = object[3].split('-')
                        date1 = date(int(object[3][0]), int(object[3][1]), int(object[3][2]))
                        object[4] = object[4].split('-')
                        date2 = date(int(object[4][0]), int(object[4][1]), int(object[4][2]))
                        
                        book = self.__book_repo.find(int(object[1]))
                        client = self.__client_repo.find(int(object[2]))                        
                        object = Rental(int(object[0]), book, client, date1, date2)
                        self.add(object)
        except FileNotFoundError:
            pass
            
    def add(self, object: IdObject):
        MemoryRepository.add(self, object)
        self.save_file()
        
    def remove(self, _id: int) -> IdObject:
        object = MemoryRepository.remove(self, _id)
        self.save_file()
        return object
    
    def update(self, object: IdObject):
        MemoryRepository.update(self, object)
        self.save_file()
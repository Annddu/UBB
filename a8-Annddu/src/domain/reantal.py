import random
from datetime import date, timedelta

from src.domain.book import Book, generate_books
from src.domain.client import Client, generate_clients
from src.domain.idobject import IdObject


# Autor: Annddu
class Rental(IdObject):
    def __init__(self, rental_id: int, book_id: Book, client_id: Client, rented_date: date, returned_date: date):
        super().__init__(rental_id)
        if not isinstance(book_id, Book):
            raise TypeError("Book id must be an integer")
        
        if not isinstance(client_id, Client):
            raise TypeError("Client id must be an integer")
        
        if not isinstance(rented_date, date) or not isinstance(returned_date, date):
            raise TypeError("Start and end must be dates")
        
        self.__book_id = book_id
        self.__client_id = client_id
        self.__start = rented_date
        self.__end = returned_date
        if self.__end > date.today():
            book_id.set_rental_status(True)            
        
    def __str__(self):
        if self.__end > date.today():
            return f"{self._id} ->  Book id: {self.__book_id._id} -> Title: {self.__book_id.title} | Author: {self.__book_id.author}  |  Client id: {self.__client_id}  |  Start: {self.__start}  |  End: {self.__end}  |  Status: Rented"
        else:
            return f"{self._id} ->  Book id: {self.__book_id}  |  Client id: {self.__client_id}  |  Start: {self.__start}  |  End: {self.__end}  |  Status: Returned"
        #return f"{self._id} ->  Book id: {self.__book_id}  |  Client id: {self.__client_id}  |  Start: {self.__start}  |  End: {self.__end}"
        
    def __repr__(self):
        return str(self)
        
    def __len__(self):
        return (self.__end - self.__start).days + 1
    
    @property
    def book(self):
        return self.__book_id
    
    @property    
    def client(self):
        return self.__client_id
    
    @property
    def rented_date(self):  
        return self.__start
    
    @property
    def returned_date(self):
        return self.__end
    
    def set_returned_date(self, date):
        self.__end = date
        self.__end = date.today()
        
def generate_rentals(number_of_rentals: int) -> list:
    books = generate_books(number_of_rentals)
    clients = generate_clients(number_of_rentals)
    _id = 500
    
    rentals = []
    for i in range(number_of_rentals):
        book = random.choice(books)
        client = random.choice(clients)
        
        start_date = date.today() + timedelta(days=random.randint(-20, -10))
        end_date = start_date + timedelta(days=random.randint(1, 30))
        
        rentals.append(Rental(_id + i, book, client, start_date, end_date))
    
    return books, clients, rentals
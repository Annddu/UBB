from src.repository.memory_repo import MemoryRepository
from src.domain.book import Book
from src.domain.client import Client
from src.domain.reantal import Rental
from src.ui.errors import *

from datetime import date


class BookRentalDTO:
    def __init__(self, book: Book, day_count: int):
        self.__book = book
        self.__days = day_count
    
    @property    
    def book(self):
        return self.__book
    
    @property
    def day_count(self):
        return self.__days
    
    def __lt__(self, other):
        return self.day_count < other.day_count
    
    def __str__(self) -> str:
        return "Rented for " + str(self.__days) + " days, book is " + str(self.__book.title) + " by " + str(self.__book.author)
    
    def __repr__(self) -> str:
        return str(self)
    
class RentalService:
    def __init__(self, rental_repo: MemoryRepository, book_repo: MemoryRepository, client_repo: MemoryRepository):
        # NB -- MemoryRepository can be replaced by any class derived from it
        # it could actually be a BinaryFileRepository(MemoryRepository),
        # or TextFileRepository(MemoryRepository)
        self.__rental_repo = rental_repo
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        
    def verify_id(self, _id: int) -> bool:
        self.__rental_repo.find(_id)
        if self.__rental_repo.find(_id) is None:
            return False
        return True
    
    def verify_if_book_is_rented(self, rental_id: int) -> bool:
        if self.__rental_repo[rental_id].returned_date > date.today():
            return True
        else:
            return False
    
    def return_book(self, rental_id: int):
        returned_date = date.today()
        self.__rental_repo[rental_id].book.set_rental_status(False)
        self.__rental_repo[rental_id].set_returned_date(returned_date)
        
    def add_rental(self, rental_id: int, book_id: int, client_id: int, rented_date: date, returned_date: date):
        book = self.__book_repo.find(book_id)
        client = self.__client_repo.find(client_id)
        rental = Rental(int(rental_id), book, client, rented_date, returned_date)
        self.__rental_repo.add(rental)
    
    def get_rentals(self) -> list:
        return self.__rental_repo.get_all()
    
    def most_rented_books(self) -> list:
        # 1. get all books
        all_books = []
        for books in self.__book_repo:  # enabled by __iter__, __next__
            all_books.append(books)

        all_rentals = []
        for rental in self.__rental_repo:
            all_rentals.append(rental)

        # 2. get all rentals for each book
        book_rentals = {}  # key = book_id, value = list of rentals
        for rental in self.__rental_repo:
            rented_book_id = rental.book.id
            if rented_book_id not in book_rentals:
                book_rentals[rented_book_id] = [rental]
            else:
                book_rentals[rented_book_id].append(rental)

        #  3. get the total rental days for each book
        book_rental_days = {}
        for book_id in book_rentals:
            book_rental_days[book_id] = 0
            for rental in book_rentals[book_id]:
                book_rental_days[book_id] += len(rental)
        
        # 4. build the DTO list
        result = []
        for book_id in book_rental_days:
            item = BookRentalDTO(self.__book_repo[book_id], book_rental_days[book_id])
            result.append(item)
        
        # 5. sort the DTO list
        result.sort(reverse=True)
    
        return result
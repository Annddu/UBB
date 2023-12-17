from src.repository.memory_repo import MemoryRepository
from src.services.rental_services import RentalService
from src.domain.book import Book
from src.ui.errors import *


class AuthorDTO:
    def __init__(self, author, day_count: int):
        self.__author = author
        self.__days = day_count
    
    @property
    def author(self):
        return self.__author
    
    @property
    def day_count(self):
        return self.__days
    
    def __lt__(self, other):
        return self.day_count < other.day_count
    
    def __str__(self) -> str:
        return "Rented for " + str(self.__days) + " days, author is " + str(self.__author)
        

class BookService:
    def __init__(self, rental_repo: MemoryRepository, book_repo: MemoryRepository):
        self.__book_repo = book_repo
        self.__rental_repo = rental_repo
    
    def verify_id(self, _id: int) -> bool:
        self.__book_repo.find(_id)
        if self.__book_repo.find(_id) is None:
            return False
        return True
    
    def verify_if_book_is_rented(self, book_id: int) -> bool:
        if self.__book_repo[book_id].rental_status == True:
            return True
        else :
            return False
    
    def add_book(self, book_id: int, title: str, author: str):
        book = Book(int(book_id), title, author)
        self.__book_repo.add(book)
    
    def remove_book(self, book_id: int):
        self.__book_repo.remove(int(book_id))
        for rental in self.__rental_repo:
            if int(rental.book.id) == int(book_id):
                self.__rental_repo.remove(int(rental.id))
    
    def update_book(self, book_id: int, title: str, author: str):
        book = Book(int(book_id), title, author)
        self.__book_repo.update(book)
    
    def get_books(self) -> list:
        return self.__book_repo.get_all()
    
    def get_book(self, book_id: int):
        return self.__book_repo.find(book_id)
    
    def search_title(self, title: str) -> list:
        result = []
        for book in self.__book_repo:
            if title.lower() in book.title.lower():
                result.append(book)
        return result
    
    def search_author(self, author: str) -> list:
        result = []
        for book in self.__book_repo:
            if author.lower() in book.author.lower():
                result.append(book)
        return result
    
    def most_rented_authors(self) -> list:
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
        
        # 4. get all authors
        all_authors = []
        for book in self.__book_repo:
            all_authors.append(book.author)
        
        # 5. get all rentals for each author from  book_rental_days
        author_rentals = {}
        for each_author in all_authors:
            author_rentals[each_author] = []
            for book_id in book_rental_days:
                if self.__book_repo[book_id].author == each_author:
                    author_rentals[each_author].append(book_rental_days[book_id])
        
        # 6. get the total rental days for each author
        author_rental_days = {}
        for each_author in author_rentals:
            author_rental_days[each_author] = 0
            for rental in author_rentals[each_author]:
                author_rental_days[each_author] += rental
        
        result = []
        for each_author in author_rental_days:
            item = AuthorDTO(each_author, author_rental_days[each_author])
            result.append(item)
            
        
            
        result.sort(reverse = True)
        
        return result
from src.repository.memory_repo import *
from src.domain.book import *
from src.domain.client import *
from src.domain.reantal import *
from src.domain.idobject import *
from src.services.rental_services import *
from src.services.book_services import *
from src.services.client_services import *

import unittest

# class TestMemoryRepository(unittest.TestCase):
#     def setUp(self):
#         self.book_repo = MemoryRepository()
#         self.client_repo = MemoryRepository()
#         self.rental_repo = MemoryRepository()
        
#         self.book1 = Book(1, "title1", "author1")
#         self.book2 = Book(2, "title2", "author2")
#         self.book3 = Book(3, "title3", "author3")
#         self.book4 = Book(4, "title4", "author4")
#         self.book5 = Book(5, "title5", "author5")
        
#         self.client1 = Client(1, "name1")
#         self.client2 = Client(2, "name2")
#         self.client3 = Client(3, "name3")
#         self.client4 = Client(4, "name4")
#         self.client5 = Client(5, "name5")
        
#         self.rental1 = Rental(1, self.book1, self.client1, date(2020, 12, 1), date(2020, 12, 5))
#         self.rental2 = Rental(2, self.book2, self.client2, date(2020, 12, 2), date(2020, 12, 6))
#         self.rental3 = Rental(3, self.book3, self.client3, date(2020, 12, 3), date(2020, 12, 7))
#         self.rental4 = Rental(4, self.book4, self.client4, date(2020, 12, 4), date(2020, 12, 8))
#         self.rental5 = Rental(5, self.book5, self.client5, date(2020, 12, 5), date(2020, 12, 9))
        
#     def test_add(self):
#         self.book_repo.add(self.book1)
#         self.book_repo.add(self.book2)
#         self.book_repo.add(self.book3)
#         self.book_repo.add(self.book4)
#         self.book_repo.add(self.book5)
        
#         self.assertEqual(len(self.book_repo), 5)
        
#     def test_remove(self):
#         self.book_repo.add(self.book1)
#         self.book_repo.add(self.book2)
#         self.book_repo.add(self.book3)
#         self.book_repo.add(self.book4)
#         self.book_repo.add(self.book5)
        
#         self.book_repo.remove(1)
#         self.book_repo.remove(2)
#         self.book_repo.remove(3)
#         self.book_repo.remove(4)
#         self.book_repo.remove(5)
        
#         self.assertEqual(len(self.book_repo), 0)
    
#     def test_update(self):
#         self.book_repo.add(self.book1)
#         self.book_repo.add(self.book2)
#         self.book_repo.add(self.book3)
#         self.book_repo.add(self.book4)
#         self.book_repo.add(self.book5)
        
#         self.book_repo.update(self.book1)
#         self.book_repo.update(self.book2)
#         self.book_repo.update(self.book3)
#         self.book_repo.update(self.book4)
#         self.book_repo.update(self.book5)
        
#         self.assertEqual(len(self.book_repo), 5)
        
#     def test_get_all(self):
#         self.book_repo.add(self.book1)
#         self.book_repo.add(self.book2)
#         self.book_repo.add(self.book3)
#         self.book_repo.add(self.book4)
#         self.book_repo.add(self.book5)
        
#         self.assertEqual(len(self.book_repo.get_all()), 5)
    
#     def test_len(self):
#         self.book_repo.add(self.book1)
#         self.book_repo.add(self.book2)
#         self.book_repo.add(self.book3)
#         self.book_repo.add(self.book4)
#         self.book_repo.add(self.book5)
        
#         self.assertEqual(len(self.book_repo), 5)
    
#     def test_iter(self):
#         self.book_repo.add(self.book1)
#         self.book_repo.add(self.book2)
#         self.book_repo.add(self.book3)
#         self.book_repo.add(self.book4)
#         self.book_repo.add(self.book5)
    
class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_repo = MemoryRepository()
        self.client_repo = MemoryRepository()
        self.rental_repo = MemoryRepository()
        
        self.book1 = Book(1, "title1", "author1")
        self.book2 = Book(2, "title2", "author2")
        self.book3 = Book(3, "title3", "author3")
        self.book4 = Book(4, "title4", "author4")
        self.book5 = Book(5, "title5", "author5")
        
        self.client1 = Client(1, "name1")
        self.client2 = Client(2, "name2")
        self.client3 = Client(3, "name3")
        self.client4 = Client(4, "name4")
        self.client5 = Client(5, "name5")
        
        self.rental1 = Rental(1, self.book1, self.client1, date(2020, 12, 1), date(2020, 12, 5))
        self.rental2 = Rental(2, self.book2, self.client2, date(2020, 12, 2), date(2020, 12, 6))
        self.rental3 = Rental(3, self.book3, self.client3, date(2020, 12, 3), date(2020, 12, 7))
        self.rental4 = Rental(4, self.book4, self.client4, date(2020, 12, 4), date(2020, 12, 8))
        self.rental5 = Rental(5, self.book5, self.client5, date(2020, 12, 5), date(2020, 12, 9))
        
        self.book_service = BookService(self.rental_repo, self.book_repo)
        
    def test_add_book(self):
        self.book_service.add_book(1, "title1", "author1")
        self.book_service.add_book(2, "title2", "author2")
        
        self.assertEqual(self.book_repo[1].title, "title1")
        self.assertEqual(self.book_repo[1].author, "author1")
        self.assertEqual(self.book_repo[2].title, "title2")
        self.assertEqual(self.book_repo[2].author, "author2")
        self.assertEqual(len(self.book_repo), 2)
        
    def test_remove_book(self):
        self.book_service.add_book(1, "title1", "author1")
        self.book_service.add_book(2, "title2", "author2")
        self.book_service.add_book(3, "title3", "author3")
        self.book_service.add_book(4, "title4", "author4")
        self.book_service.add_book(5, "title5", "author5")
        
        self.assertEqual(len(self.book_repo), 5)
        
        self.book_service.remove_book(1)
        self.book_service.remove_book(2)
        self.book_service.remove_book(3)
        self.book_service.remove_book(4)
        self.book_service.remove_book(5)
        
        self.assertEqual(len(self.book_repo), 0)
        
    def test_update_book(self):
        self.book_service.add_book(1, "title1", "author1")       
        self.book_service.update_book(1, "title2", "author2")
        
        self.assertEqual(len(self.book_repo), 1)
        
        self.assertEqual(self.book_repo[1].title, "title2")
        self.assertEqual(self.book_repo[1].author, "author2")
        
        self.assertEqual(len(self.book_repo), 1)

class TestClientService(unittest.TestCase):
    def setUp(self):
        self.book_repo = MemoryRepository()
        self.client_repo = MemoryRepository()
        self.rental_repo = MemoryRepository()
        
        self.book1 = Book(1, "title1", "author1")
        self.book2 = Book(2, "title2", "author2")
        self.book3 = Book(3, "title3", "author3")
        self.book4 = Book(4, "title4", "author4")
        self.book5 = Book(5, "title5", "author5")
        
        self.client1 = Client(1, "name1")
        self.client2 = Client(2, "name2")
        self.client3 = Client(3, "name3")
        self.client4 = Client(4, "name4")
        self.client5 = Client(5, "name5")
        
        self.rental1 = Rental(1, self.book1, self.client1, date(2020, 12, 1), date(2020, 12, 5))
        self.rental2 = Rental(2, self.book2, self.client2, date(2020, 12, 2), date(2020, 12, 6))
        self.rental3 = Rental(3, self.book3, self.client3, date(2020, 12, 3), date(2020, 12, 7))
        self.rental4 = Rental(4, self.book4, self.client4, date(2020, 12, 4), date(2020, 12, 8))
        self.rental5 = Rental(5, self.book5, self.client5, date(2020, 12, 5), date(2020, 12, 9))
        
        self.client_service = ClientService(self.rental_repo, self.client_repo)
        
    def test_add_client(self):
        self.client_service.add_client(1, "name1")
        self.client_service.add_client(2, "name2")
        
        self.assertEqual(self.client_repo[1].name, "name1")
        self.assertEqual(self.client_repo[2].name, "name2")
        self.assertEqual(len(self.client_repo), 2)
        
    def test_remove_client(self):
        self.client_service.add_client(1, "name1")
        self.client_service.add_client(2, "name2")
        self.client_service.add_client(3, "name3")
        self.client_service.add_client(4, "name4")
        self.client_service.add_client(5, "name5")
        
        self.assertEqual(len(self.client_repo), 5)
        
        self.client_service.remove_client(1)
        self.client_service.remove_client(2)
        self.client_service.remove_client(3)
        self.client_service.remove_client(4)
        self.client_service.remove_client(5)
        
        self.assertEqual(len(self.client_repo), 0)
    
    def test_update_client(self):
        self.client_service.add_client(1, "name1")
        self.client_service.update_client(1, "name2")
        
        self.assertEqual(len(self.client_repo), 1)
        
        self.assertEqual(self.client_repo[1].name, "name2")
        
        self.assertEqual(len(self.client_repo), 1)
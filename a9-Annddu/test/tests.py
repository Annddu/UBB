from src.repository.memory_repo import *
from src.domain.book import *
from src.domain.client import *
from src.domain.reantal import *
from src.domain.idobject import *
from src.services.rental_services import *
from src.services.book_services import *
from src.services.client_services import *
from src.services.undo_redo_services import *

import unittest
    
class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_repo = MemoryRepository()
        self.client_repo = MemoryRepository()
        self.rental_repo = MemoryRepository()
        self.undo_redo_service = UndoRedoService()
        
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
        
        self.book_service = BookService(self.rental_repo, self.book_repo, self.undo_redo_service)
        
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
        self.undo_redo_service = UndoRedoService()
        
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
        
        self.client_service = ClientService(self.rental_repo, self.client_repo, self.undo_redo_service)
        
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
        
class TestUndoRedoServiceBook(unittest.TestCase):
    def setUp(self):
        self.book_repo = MemoryRepository()
        self.client_repo = MemoryRepository()
        self.rental_repo = MemoryRepository()
        self.undo_redo_service = UndoRedoService()
        
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
        
        self.book_service = BookService(self.rental_repo, self.book_repo, self.undo_redo_service)
        self.client_service = ClientService(self.rental_repo, self.client_repo, self.undo_redo_service)
        
    def test_undo_add_book(self):
        self.book_service.add_book(1, "title1", "author1")
        self.book_service.add_book(2, "title2", "author2")
        self.book_service.add_book(3, "title3", "author3")
        self.book_service.add_book(4, "title4", "author4")
        self.book_service.add_book(5, "title5", "author5")
        
        self.assertEqual(len(self.book_repo), 5)
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.book_repo), 4)
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.book_repo), 3)
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.book_repo), 4)
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.book_repo), 5)
        
    def test_undo_remove_book(self):
        self.book_service.add_book(1, "title1", "author1")
        self.book_service.add_book(2, "title2", "author2")
        self.book_service.add_book(3, "title3", "author3")
        self.book_service.add_book(4, "title4", "author4")
        self.book_service.add_book(5, "title5", "author5")
        
        self.assertEqual(len(self.book_repo), 5)
        
        self.book_service.remove_book(1)
        self.book_service.remove_book(2)
        
        self.assertEqual(len(self.book_repo), 3)
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.book_repo), 4)
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.book_repo), 5)
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.book_repo), 4)
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.book_repo), 3)
        
    def test_undo_update_book(self):
        self.book_service.add_book(1, "title1", "author1")
        self.book_service.add_book(2, "title2", "author2")
        self.book_service.add_book(3, "title3", "author3")
        self.book_service.add_book(4, "title4", "author4")
        self.book_service.add_book(5, "title5", "author5")
        
        self.assertEqual(len(self.book_repo), 5)
        
        self.book_service.update_book(1, "title6", "author6")
        self.book_service.update_book(2, "title7", "author7")
        
        self.assertEqual(len(self.book_repo), 5)
        self.assertEqual(self.book_repo[1].title, "title6")
        self.assertEqual(self.book_repo[1].author, "author6")
        self.assertEqual(self.book_repo[2].title, "title7")
        self.assertEqual(self.book_repo[2].author, "author7")
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.book_repo), 5)
        self.assertEqual(self.book_repo[2].title, "title2")
        self.assertEqual(self.book_repo[2].author, "author2")
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.book_repo), 5)
        self.assertEqual(self.book_repo[1].title, "title1")
        self.assertEqual(self.book_repo[1].author, "author1")
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.book_repo), 5)
        self.assertEqual(self.book_repo[1].title, "title6")
        self.assertEqual(self.book_repo[1].author, "author6")
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.book_repo), 5)
        self.assertEqual(self.book_repo[2].title, "title7")
        self.assertEqual(self.book_repo[2].author, "author7")

class TestUndoRedoServiceClient(unittest.TestCase):
    def setUp(self):
        self.book_repo = MemoryRepository()
        self.client_repo = MemoryRepository()
        self.rental_repo = MemoryRepository()
        self.undo_redo_service = UndoRedoService()
        
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
        
        self.book_service = BookService(self.rental_repo, self.book_repo, self.undo_redo_service)
        self.client_service = ClientService(self.rental_repo, self.client_repo, self.undo_redo_service)
        
    def test_undo_add_client(self):
        self.client_service.add_client(1, "name1")
        self.client_service.add_client(2, "name2")
        self.client_service.add_client(3, "name3")
        self.client_service.add_client(4, "name4")
        self.client_service.add_client(5, "name5")
        
        self.assertEqual(len(self.client_repo), 5)
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.client_repo), 4)
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.client_repo), 3)
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.client_repo), 4)
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.client_repo), 5)
        
    def test_undo_remove_client(self):
        self.client_service.add_client(1, "name1")
        self.client_service.add_client(2, "name2")
        self.client_service.add_client(3, "name3")
        self.client_service.add_client(4, "name4")
        self.client_service.add_client(5, "name5")
        
        self.assertEqual(len(self.client_repo), 5)
        
        self.client_service.remove_client(1)
        self.client_service.remove_client(2)
        
        self.assertEqual(len(self.client_repo), 3)
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.client_repo), 4)
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.client_repo), 5)
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.client_repo), 4)
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.client_repo), 3)
        
    def test_undo_update_client(self):
        self.client_service.add_client(1, "name1")
        self.client_service.add_client(2, "name2")
        self.client_service.add_client(3, "name3")
        self.client_service.add_client(4, "name4")
        self.client_service.add_client(5, "name5")
        
        self.assertEqual(len(self.client_repo), 5)
        
        self.client_service.update_client(1, "name6")
        self.client_service.update_client(2, "name7")
        
        self.assertEqual(len(self.client_repo), 5)
        self.assertEqual(self.client_repo[1].name, "name6")
        self.assertEqual(self.client_repo[2].name, "name7")
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.client_repo), 5)
        self.assertEqual(self.client_repo[2].name, "name2")
        
        self.undo_redo_service.undo()
        
        self.assertEqual(len(self.client_repo), 5)
        self.assertEqual(self.client_repo[1].name, "name1")
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.client_repo), 5)
        self.assertEqual(self.client_repo[1].name, "name6")
        
        self.undo_redo_service.redo()
        
        self.assertEqual(len(self.client_repo), 5)
        self.assertEqual(self.client_repo[2].name, "name7")
        
# class TestUndoRedoServiceRental(unittest.TestCase):
#     def setUp(self):
#         self.book_repo = MemoryRepository()
#         self.client_repo = MemoryRepository()
#         self.rental_repo = MemoryRepository()
#         self.undo_redo_service = UndoRedoService()
        
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
        
#         self.book_service = BookService(self.rental_repo, self.book_repo, self.undo_redo_service)
#         self.client_service = ClientService(self.rental_repo, self.client_repo, self.undo_redo_service)
#         self.rental_service = RentalService(self.rental_repo, self.book_repo, self.client_repo, self.undo_redo_service)
        
#     def test_undo_rent_book(self):
#         self.book_service.add_book(1, "title1", "author1")
#         self.client_service.add_client(1, "name1")
        
#         self.rental_service.rent_book(1, 1, 1, date(2020, 12, 1), date(2020, 12, 5))
        
#         self.assertEqual(len(self.rental_repo), 1)
        
#         self.undo_redo_service.undo()
        
#         self.assertEqual(len(self.rental_repo), 0)
        
#         self.undo_redo_service.redo()
        
#         self.assertEqual(len(self.rental_repo), 1)
        
#     def test_undo_return_rental(self):
#         self.book_service.add_book(1, "title1", "author1")
#         self.client_service.add_client(1, "name1")
        
#         self.rental_service.rent_book(1, 1, 1, date(2020, 12, 1), date(2020, 12, 5))
        
#         self.assertEqual(len(self.rental_repo), 1)
        
#         self.rental_service.return_book(1)
        
#         self.assertEqual(len(self.rental_repo), 1)
        
#         self.undo_redo_service.undo()
        
#         self.assertEqual(len(self.rental_repo), 1)
        
#         self.undo_redo_service.redo()
        
#         self.assertEqual(len(self.rental_repo), 1)
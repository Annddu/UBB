from src.repository.memory_repo import MemoryRepository
from src.repository.memory_repo import Pickle
from src.repository.memory_repo import TextRepository
from src.services.rental_services import RentalService
from src.services.book_services import BookService
from src.services.client_services import ClientService
from src.services.undo_redo_services import UndoRedoService
from src.domain.reantal import generate_rentals
from src.ui.ui import UI
from src.ui.gui import GUI
from test.tests import *
import configparser
import os

configFilePath = r'D:\UBB\a9-Annddu\settings.properties'

config = configparser.RawConfigParser()
config.read(configFilePath)
config.sections()
repository = config.get('Settings', 'repository')
book_file = config.get('Settings', 'books')
client_file = config.get('Settings', 'clients')
rental_file = config.get('Settings', 'rentals')

if repository == "memory":
    book_repo = MemoryRepository()
    client_repo = MemoryRepository()
    rental_repo = MemoryRepository()
    books, clients, rentals = generate_rentals(20)
    for book in books:
        book_repo.add(book)
        
    for client in clients:
        client_repo.add(client)

    for rental in rentals:
        rental_repo.add(rental)
    
elif repository == "pickle":
    book_repo = Pickle(book_file)
    client_repo = Pickle(client_file)
    rental_repo = Pickle(rental_file)
    
elif repository == "text":
    book_repo = TextRepository(book_file)
    client_repo = TextRepository(client_file)
    rental_repo = TextRepository(rental_file, book_repo, client_repo)
 
undo_redo_service = UndoRedoService()   
rental_service = RentalService(rental_repo, book_repo, client_repo, undo_redo_service)
client_service = ClientService(rental_repo ,client_repo, undo_redo_service)
book_service = BookService(rental_repo, book_repo, undo_redo_service)

ui = UI(rental_service, book_service, client_service, undo_redo_service)
ui.run()
unittest.main()

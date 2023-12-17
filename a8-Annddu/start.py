from src.repository.memory_repo import MemoryRepository
from src.services.rental_services import RentalService
from src.services.book_services import BookService
from src.services.client_services import ClientService
from src.domain.reantal import generate_rentals
from src.ui.ui import UI
from src.ui.gui import GUI
from test.tests import *

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
    
rental_service = RentalService(rental_repo, book_repo, client_repo)
client_service = ClientService(rental_repo ,client_repo)
book_service = BookService(rental_repo, book_repo)

ui = UI(rental_service, book_service, client_service)
ui.run()
unittest.main()

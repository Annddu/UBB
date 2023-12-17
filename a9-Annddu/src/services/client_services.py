from src.repository.memory_repo import MemoryRepository
from src.services.undo_redo_services import FunctionCall, Operation, CascadingOperation 
from src.domain.client import Client
from src.domain.reantal import Rental
from src.ui.errors import *


class ClientDTO:
    def __init__(self, client: Client, day_count: int):
        self.__client = client
        self.__days = day_count
        
    @property
    def client(self):
        return self.__client
    
    @property
    def day_count(self):
        return self.__days
    
    def __lt__(self, other):
        return self.day_count < other.day_count
    
    def __str__(self) -> str:
        return "The client " + str(self.__client.name) + " has rented books for " + str(self.__days) + " days"
        
    def __repr__(self) -> str:
        return str(self)

class ClientService:
    def __init__(self, rental_repo: MemoryRepository ,client_repo: MemoryRepository, undo_redo_service):
        self.__client_repo = client_repo
        self.__rental_repo = rental_repo
        self._undo_redo_service = undo_redo_service
    
    def verify_id(self, _id: int) -> bool:
        self.__client_repo.find(_id)
        if self.__client_repo.find(_id) is None:
            return False
        return True
    
    def add_client(self, client_id: int, name: str):
        client = Client(int(client_id), name)
        self.__client_repo.add(client)   
        
        redo = FunctionCall(self.__client_repo.add, client)
        undo = FunctionCall(self.__client_repo.remove, int(client_id))
        operation = Operation(undo, redo)
        self._undo_redo_service.recordOperation(operation) 
    
    def remove_client(self, client_id: int):
        client = self.__client_repo.remove(int(client_id))
        redo = FunctionCall(self.__client_repo.remove, int(client_id))
        undo = FunctionCall(self.__client_repo.add, client)
        operation = Operation(undo, redo)
        
        operations = [operation]
        
        for rental in self.__rental_repo:
            if int(rental.client.id) == int(client_id):
                rental = self.__rental_repo.remove(int(rental.id))
                redo = FunctionCall(self.__rental_repo.remove, int(rental.id))
                undo = FunctionCall(self.__rental_repo.add, rental)
                operation_rental = Operation(undo, redo)
                operations.append(operation_rental)
                
        cascading_operation = CascadingOperation(operations)
        self._undo_redo_service.recordOperation(cascading_operation)
        
    def update_client(self, client_id: int, name: str):
        old_client = self.__client_repo.__getitem__(int(client_id))
        client = Client(int(client_id), name)
        self.__client_repo.update(client)
        
        redo = FunctionCall(self.__client_repo.update, client)
        undo = FunctionCall(self.__client_repo.update, old_client)
        operation = Operation(undo, redo)
        
        operations = [operation]
        
        for rental in self.__rental_repo:
            if int(rental.client.id) == int(client_id):
                old_rental = rental
                new_rental = Rental(rental.id, rental.book, client, rental.rented_date, rental.returned_date)
                self.__rental_repo.update(new_rental)
                redo_rental = FunctionCall(self.__rental_repo.update, new_rental)
                undo_rental = FunctionCall(self.__rental_repo.update, old_rental)
                operation_rental = Operation(undo_rental, redo_rental)
                operations.append(operation_rental)
        
        cascading_operation = CascadingOperation(operations)
        self._undo_redo_service.recordOperation(cascading_operation)
    
    def get_clients(self) -> list:
        return self.__client_repo.get_all()
    
    def get_client(self, client_id: int):
        return self.__client_repo.find(client_id)
    
    def search_name(self, name: str) -> list:
        result = []
        for client in self.__client_repo:
            if name in client.name:
                result.append(client)
        return result
    
    def most_active_clients(self) -> list:
        # 1. get all clients
        all_clients = []
        for clients in self.__client_repo:  # enabled by __iter__, __next__
            all_clients.append(clients)
        
        all_rentals = []
        for rental in self.__rental_repo:
            all_rentals.append(rental)
            
        # 2. get all rentals for each client
        client_rentals = {}
        for rental in self.__rental_repo:
            rented_client_id = rental.client.id
            if rented_client_id not in client_rentals:
                client_rentals[rented_client_id] = []
            else:	
                client_rentals[rented_client_id].append(rental)
        
        # 3. get the total rental days for each client
        client_rental_days = {}
        for client_id in client_rentals:
            client_rental_days[client_id] = 0
            for rental in client_rentals[client_id]:
                client_rental_days[client_id] += len(rental)
                
        #4. sort them desc (use a DTO - data transfer object)
        result = []
        for client_id in client_rental_days:
            item = ClientDTO(self.__client_repo[client_id], client_rental_days[client_id])
            result.append(item)
            
        result.sort(reverse = True)
        
        return result
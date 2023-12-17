import random

from src.domain.idobject import IdObject

# Autor: Annddu
class Client(IdObject):
    def __init__(self, client_id: int, name: str):
        super().__init__(client_id)
        if not isinstance(name, str):
            raise TypeError("The name must be a string.")
        self.__name = name
        
    def __str__(self):
        return f"{self._id} ->  Name: {self.__name}"
    
    def __eq__(self, other) -> bool:
        return self.id == other.id
    
    @property
    def name(self) -> str:
        return self.__name
    
def generate_clients(n: int) -> list:
    _id = 200
    family_names = ['Smith', 'Jones', 'Williams', 'Taylor', 'Brown', 'Wilson', 'Davies', 'Evans', 'Thomas', 'Johnson']
    given_names = ["Oliver", "William", "Jack", "Harry", "Leo", "Olivia", "Amelia", "Evelyn", "Grace", "Sophie"]
    result = []
    for i in range(n):
        result.append(Client(_id + i, random.choice(family_names) + " " + random.choice(given_names)))
    return result

# for client in generate_clients(20):
#     print(client)
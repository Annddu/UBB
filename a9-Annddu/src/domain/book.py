import random
from src.domain.idobject import IdObject


# Autor: Annddu
class Book(IdObject):
    def __init__(self, book_id: int, title: str, author: str):
        super().__init__(book_id)
        self.__title = title
        self.__author = author
        self.__rented = False
        
    def __str__(self):
        return f"{self._id} ->  Title: {self.title}  |  Author: {self.author} |  Rental status: {self.__rented}" 
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.get_id() == other.get_id()
    
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def author(self) -> str:
        return self.__author
    
    @property
    def rental_status(self) -> bool:
        return self.__rented
    
    def set_rental_status(self, status: bool):
        self.__rented = status
    
def generate_books(number_of_books: int) -> list:
    _id = 100
    books_list = []
    random_books = [["Liviu Rebreanu", "Ion", "Pădurea spânzuraților", "Ciuleandra"], ["Mihai Eminescu", "Luceafărul", "Scrisoarea III", "Floare albastră"], 
                    ["Ion Creangă", "Amintiri din copilărie", "Povestea lui Harap-Alb", "Povestea lui Țepeș Vodă"], ["George Coșbuc", "Moartea lui Fulger", "Miorița", "Lupta vieții"], 
                    ["Mihail Sadoveanu", "Baltagul", "Hanu Ancuței", "Creanga de aur"], ["Lucian Blaga", "Eu nu strivesc corola de minuni a lumii", "La cumpăna apelor", "În marea trecere"], 
                    ["George Bacovia", "Plumb", "Amurg violet", "Lacustră"], ["Ion Luca Caragiale", "O scrisoare pierdută", "D-ale carnavalului", "O noapte furtunoasă"], 
                    ["Tudor Arghezi", "Flori de mucigai", "Cartea cu jucării", "Cărticica de seară"], ["Nicolae Labiș", "Moartea căprioarei", "Cântec", "Către toamnă"], 
                    ["George Topârceanu", "Bunica", "Răspuns", "Iarna pe uliță"], ["Vasile Alecsandri", "Hora Unirii", "Miezul iernii", "Oaspeții primăverii"], 
                    ["Ion Minulescu", "Joc secund", "Ceasornicul", "Omul de lut"], ["Octavian Goga", "Rugăciune", "Sunt mândru că sunt român", "Doină"], 
                    ["Ion Barbu", "Riga Crypto și Lapona Enigel", "Joc secund", "În ceasul al doisprezecelea"]]
    for i in range(number_of_books):
        random_number = random.randint(0, len(random_books)-1)
        books_list.append( Book (_id + i, f'{random.choice(random_books[random_number][1:])}', f'{random.choice(random_books[random_number][:1])}' ) )
    return books_list

# for book in generate_books(20):
#     print(book)
# books = generate_books(20)

# # Convert the list of books to a list of tuples for tabulate
# table_data = [(book.get_id(), book.title, book.author) for book in books]

# # Define the headers for the table
# headers = ["ID", "Title", "Author"]

# # Print the table
# print(tabulate.tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
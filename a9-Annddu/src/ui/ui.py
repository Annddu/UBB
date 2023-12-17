from src.ui.errors import *
from datetime import date

class UI:
    def __init__(self, services_rental, services_book, services_client, undo_redo_service):
        self.__services_book = services_book
        self.__services_client = services_client
        self.__services_rental = services_rental
        self._undo_redo_service = undo_redo_service
    
    def print_menu(self):
        print("\nMenu:")
        print("1. Book operations")
        print("2. Client operations")
        print("3. Rental operations")
        print("4. Search")
        print("5. Statistics")
        print("6. Exit")
        print("7. Undo")
        print("8. Redo")
        
    def print_book_menu(self):
        print("\nBook operations:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Update a book")
        print("4. Display the list of books")
        print("6. Exit")
        
    def print_client_menu(self):
        print("\nClient operations:")
        print("1. Add a client")
        print("2. Remove a client")
        print("3. Update a client")
        print("4. Display the list of clients")
        print("6. Exit")
    
    def print_rental_menu(self):
        print("\nRental operations:")
        print("1. Rent a book")
        print("2. Return a book")
        print("3. Display the list of rentals")
        print("6. Exit")
        
    def print_search_menu(self):
        print("\nSearch:")
        print("1. Search books")
        print("2. Search clients")
        print("6. Exit")
    
    def print_search_books_menu(self):
        print("\nSearch books:")
        print("1. Search by id")
        print("2. Search by title")
        print("3. Search by author")
        print("6. Exit")
        
    def print_search_clients_menu(self):
        print("\nSearch clients:")
        print("1. Search by id")
        print("2. Search by name")
        print("6. Exit")
        
    def print_statistics_menu(self):
        print("\nStatistics:")
        print("1. Most rented books")
        print("2. Most active clients")
        print("3. Most rented authors")
        print("6. Exit")
    
    # Book operations
    def add_book(self):
        while True:
            try:
                book_id = input("Enter the book id: ")
                while self.__services_book.verify_id(int(book_id)):
                    book_id = input("Enter a new book id: ")
                title = input("Enter the book title: ")
                author = input("Enter the book author: ")
                self.__services_book.add_book(book_id, title, author)
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Book id must be an integer and the title/author a string!")
            else:
                print("Book added successfully!")
                break
    
    def remove_book(self):
        while True:
            try:
                book_id = input("Enter the book id: ")
                while not self.__services_book.verify_id(int(book_id)):
                    book_id = input("Enter an existing book id: ")
                self.__services_book.remove_book(book_id)
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Book id must be an integer!")
            else:
                print("Book removed successfully!")
                break
    
    def update_book(self):
        while True:
            try:
                book_id = input("Enter the book id: ")
                title = input("Enter the book title: ")
                author = input("Enter the book author: ")
                self.__services_book.update_book(book_id, title, author)
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Book id must be an integer and the title/author a string!")
            else:
                print("Book updated successfully!")
                break
    
    def display_books(self):
        for book in self.__services_book.get_books():
            print(book)
       
    # Client operations
    
    def add_client(self):
        while True:
            try:
                client_id = input("Enter the client id: ")
                while self.__services_client.verify_id(int(client_id)):
                    client_id = input("Enter a new client id: ")
                name = input("Enter the client name: ")
                self.__services_client.add_client(client_id, name)
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Client id must be an integer and the name a string!")
            else:
                print("Client added successfully!")
                break
    
    def remove_client(self):
        while True:
            try:
                client_id = input("Enter the client id: ")
                while not self.__services_client.verify_id(int(client_id)):
                    client_id = input("Enter an existing client id: ")
                self.__services_client.remove_client(client_id)
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Client id must be an integer!")
            else:
                print("Client removed successfully!")
                break
    
    def update_client(self):
        while True:
            try:
                client_id = input("Enter the client id: ")
                name = input("Enter the client name: ")
                self.__services_client.update_client(client_id, name)
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Client id must be an integer and the name a string!")
            else:
                print("Client updated successfully!")
                break
    
    def display_clients(self):
        for client in self.__services_client.get_clients():
            print(client)
    
    # Rental operations
    
    def rent_book(self):
        print("The book will be rented from today until the due date you specify!")
        while True:
            try:
                rental_id = input("Enter the rental id: ")
                int(rental_id)
                while  self.__services_rental.verify_id(int(rental_id)):
                    rental_id = input("Enter a new rental id: ")
                
                book_id = input("Enter the book id: ")
                int(book_id)
                while not self.__services_book.verify_id(int(book_id)) or self.__services_book.verify_if_book_is_rented(int(book_id)):
                    book_id = input("Enter an existing and also unrented book id : ")
                
                client_id = input("Enter the client id: ")
                int(client_id)
                while not self.__services_client.verify_id(int(client_id)):
                    client_id = input("Enter an existing client id: ")
                    
                due_date = input("Enter the due date (dd.mm.yyyy): ")
                due_date = due_date.split(".")
                due_date = date(int(due_date[2]), int(due_date[1]), int(due_date[0]))
                while due_date < date.today():
                    due_date = input("Enter a valid due date (dd.mm.yyyy): ")
                    due_date = due_date.split(".")
                    due_date = date(int(due_date[2]), int(due_date[1]), int(due_date[0]))
                
                rented_date = date.today()
                returned_date = due_date
                self.__services_rental.add_rental(rental_id, int(book_id), int(client_id), rented_date, returned_date)
                    
            except ValidationException as e:
                print(e)
            except IndexError:
                print("The date must be in the format dd.mm.yyyy!")
            except ValueError:
                print("Rental id must be an integer and the dates must be in the format dd.mm.yyyy!")
            else:
                print("Book rented successfully!")
                break
    
    def return_book(self):
        while True:
            try:
                rental_id = input("Enter the rental id: ")
                int(rental_id)
                while not self.__services_rental.verify_id(int(rental_id)) or not self.__services_rental.verify_if_book_is_rented(int(rental_id)):
                    rental_id = input("Enter an existing rental id wich is stil not returned: ")

                self.__services_rental.return_book(int(rental_id))
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Rental id must be an integer!")
            else:
                print("Book returned successfully!")
                break
    
    def display_rentals(self):
        for rental in self.__services_rental.get_rentals():
            print(rental)
    
    # Search
    
    def search_books(self):
        while True:
            try:
                self.print_search_books_menu()
                choice = input("Enter your choice: ")
                if choice == "6":
                    break
                
                elif choice == "1":
                    while True:
                        try:
                            book_id = input("Enter the book id: ")
                            int(book_id)
                            if not self.__services_book.verify_id(int(book_id)):
                                print("Book id does not exist!")
                            else:
                                print(self.__services_book.get_book(int(book_id)))
                        except ValueError:
                            print("Book id must be an integer!")
                        else:
                            break
                    
                elif choice == "2":
                    while True:
                        try:
                            title = input("Enter the book title: ")
                            result = self.__services_book.search_title(title)
                            if len(result) == 0:
                                print("No books found!")
                            else:
                                for book in result:
                                    print(book)
                        except ValueError:
                            print("Book title must be a string!")
                        else:
                            break
                    
                elif choice == "3":
                    while True:
                            try:
                                author = input("Enter the book author: ")
                                result = self.__services_book.search_author(author)
                                if len(result) == 0:
                                    print("No books found!")
                                else:
                                    for book in result:
                                        print(book)
                            except ValueError:
                                print("Book author must be a string!")
                            else:
                                break   
                else:
                    print("Invalid choice!")
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Book id must be an integer and the title/author a string!")
            else:
                break   
                
    def search_clients(self):
        while True:
            try:
                self.print_search_clients_menu()
                choice = input("Enter your choice: ")
                if choice == "6":
                    break
                elif choice == "1":
                    while True:
                        try:
                            client_id = input("Enter the client id: ")
                            int(client_id)
                            if not self.__services_client.verify_id(int(client_id)):
                                print("Client id does not exist!")
                            else:
                                print(self.__services_client.get_client(int(client_id)))
                        except ValueError:
                            print("Book id must be an integer!")
                        else:
                            break
                elif choice == "2":
                    while True:
                        try:
                            name = input("Enter the client name: ")
                            result = self.__services_client.search_name(name)
                            if len(result) == 0:
                                print("No clients found!")
                            else:
                                for client in result:
                                    print(client)
                        except ValueError:
                            print("Client name must be a string!")
                        else:
                            break
                else:
                    print("Invalid choice!")
            except ValidationException as e:
                print(e)
            except ValueError:
                print("Client id must be an integer and the name a string!")
            else:
                break
    
    # Statistics
    def most_rented_books(self):
        result = self.__services_rental.most_rented_books()
        for book in result:
            print(book)
            
    def most_active_clients(self):
        result = self.__services_client.most_active_clients()
        for client in result:
            print(client)
            
    def most_rented_authors(self):
        result = self.__services_book.most_rented_authors()
        for author in result:
            print(author)
        
    def book_operations(self):
        while True:
            self.print_book_menu()
            choice = input("Enter your choice: ")
            if choice == "6":
                break
            elif choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.update_book()
            elif choice == "4":
                self.display_books()
            else:
                print("Invalid choice!")
    
    def client_operations(self):
        while True:
            self.print_client_menu()
            choice = input("Enter your choice: ")
            if choice == "6":
                break
            elif choice == "1":
                self.add_client()
            elif choice == "2":
                self.remove_client()
            elif choice == "3":
                self.update_client()
            elif choice == "4":
                self.display_clients()
            else:
                print("Invalid choice!")
    
    def rental_operations(self):
        while True:
            self.print_rental_menu()
            choice = input("Enter your choice: ")
            if choice == "6":
                break
            elif choice == "1":
                self.rent_book()
            elif choice == "2":
                self.return_book()
            elif choice == "3":
                self.display_rentals()
            else:
                print("Invalid choice!")
    
    def search(self):
        while True:
            self.print_search_menu()
            choice = input("Enter your choice: ")
            if choice == "6":
                break
            elif choice == "1":
                self.search_books()
            elif choice == "2":
                self.search_clients()
            else:
                print("Invalid choice!")
    
    def statistics(self):
        while True:
            self.print_statistics_menu()
            choice = input("Enter your choice: ")
            if choice == "6":
                break
            elif choice == "1":
                self.most_rented_books()
            elif choice == "2":
                self.most_active_clients()
            elif choice == "3":
                self.most_rented_authors()
            else:
                print("Invalid choice!")
    
    def undo(self):
        try:
            self._undo_redo_service.undo()
        except UndoError as e:
            print(e)
    
    def redo(self):
        try:
            self._undo_redo_service.redo()
        except RedoError as e:
            print(e)
        
    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")
            if choice == "6":
                break
            elif choice == "1":
                self.book_operations()
            elif choice == "2":
                self.client_operations()
            elif choice == "3":
                self.rental_operations()
            elif choice == "4":
                self.search()
            elif choice == "5":
                self.statistics()
            elif choice == "7":
                self.undo()
            elif choice == "8":
                self.redo()
            else:
                print("Invalid choice!")
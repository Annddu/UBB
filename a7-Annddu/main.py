from src.ui.ui_class import *
from src.repository.memoryrep import *
from src.services.services import *
from src.domain.student import *
from src.testing.test import *

if __name__ == "__main__":
    # Initialize repositories
    memory_repository = MemoryRepository()
    text_file_repository = TextFileRepository("students.txt")
    binary_file_repository = PickleRepository("students.pkl")
    
    for i in range(1, 11):
        memory_repository.add_student(Student(i, "Student " + str(i), i%3 + 1))

    # Initialize services with the desired repository
    services = Services(binary_file_repository)

    ui = UI(services)
    ui.run()
    
    text_file_repository.save_data()
    binary_file_repository.save_data()
    unittest.main()
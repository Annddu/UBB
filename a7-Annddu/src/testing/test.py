from src.repository.memoryrep import *
from src.services.services import *

import unittest

class TestServices(unittest.TestCase):
    """
    Unit test class for Services
    """
    def setUp(self):
        # Set up a test repository (can be MemoryRepository, TextFileRepository, etc.)
        self.test_repository = MemoryRepository()
        self.test_services = Services(self.test_repository)

    def test_add_student(self):
        # Test adding a student
        self.test_services.add_student(1, "Andu", 1)
        students = self.test_repository.get_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Andu")

    def test_filter_students_by_group(self):
        # Test filtering students by group
        self.test_services.add_student(1, "Andu", 1)
        self.test_services.add_student(2, "Maria", 2)
        self.test_services.filter_students_by_group(1)
        students = self.test_repository.get_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Maria")

    def test_undo_last_operation(self):
        # Test undoing the last operation
        self.test_services.add_student(1, "Andu", 1)
        self.test_services.undo_last_operation()
        students = self.test_repository.get_students()
        self.assertEqual(len(students), 1)

    def test_undo_last_operation_multiple(self):
        # Test undoing multiple operations
        self.test_services.add_student(1, "Andu", 1)
        self.test_services.add_student(2, "Andu", 2)
        self.test_services.undo_last_operation()
        students = self.test_repository.get_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Andu")

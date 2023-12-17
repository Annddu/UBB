from src.domain.student import *

class Services:
    def __init__(self, repository):
        self.repository = repository

    def add_student(self, student_id, name, group):
        """	
        1. Adds a student to the list of students.
        """
        self.repository.add_student(student = Student(student_id, name, group))
        

    def display_students(self):
        """
        2. Displays the list of students.
        """
        students = self.repository.get_students()
        for student in students:
            print(student)

    def filter_students_by_group(self, group):
        """
        3. Filters the students list by group.
        """
        self.repository.delete_students_in_group(group)

    def undo_last_operation(self):
        """	
        4. Undoes the last operation that changed the list of students.
        """
        self.repository.undo_last_operation()
        
    def verify_student_id(self, student_id):
        """
        Verifies if a student with the given ID exists in the repository.
        """	
        students = self.repository.get_students()
        for student in students:
            if student.student_id == student_id:
                return True
        return False
    
    def verify_student_group(self, group):
        """
        Verifies if a group with the given ID exists in the repository.
        """	
        students = self.repository.get_students()
        for student in students:
            if student.group == group:
                return True
        return False
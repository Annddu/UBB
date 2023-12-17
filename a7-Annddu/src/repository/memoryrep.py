import ast
import pickle
import copy
import os

from src.domain.student import Student

class MemoryRepository:
    def __init__(self):
        self.students = []
        self.history = [self.students]

    def add_student(self, student):
        self.students.append(student)
        self.history.append(copy.deepcopy(self.students))

    def delete_students_in_group(self, group):
        self.students = [student for student in self.students if student.group != group]
        self.history.append(copy.deepcopy(self.students))

    def get_students(self):
        return self.students

    def undo_last_operation(self):
        if len(self.history) > 1:
            self.history.pop()
            self.students = copy.deepcopy(self.history[-1])
        else:
            raise ValueError

class TextFileRepository:
    def __init__(self, filename):
        self.students = []
        self.history = [self.students]
        self.filename = filename
        self.__load_file()
        
    # def load_data(self):
    #     try:
    #         with open(self.filename, 'r') as file:
    #             data = file.read()
    #             self.students = ast.literal_eval(data)
    #             self.history = [self.students]
    #     except FileNotFoundError:
    #         pass
    #     except SyntaxError:
    #         pass
        
    def save_data(self):
        self.File_object = open(self.filename ,"w")
        strings = ''
        for each in self.students:
            strings += f"{each.student_id},{each.name},{each.group} \n"
        self.File_object.write(strings)
        self.File_object.close()

    def add_student(self, student):
        self.students.append(student)
        self.history.append(copy.deepcopy(self.students))
        self.save_data()

    def delete_students_in_group(self, group):
        self.students = [student for student in self.students if student.group != group]
        self.history.append(copy.deepcopy(self.students))
        self.save_data()

    def get_students(self):
        return self.students
    
    def undo_last_operation(self):
        if len(self.history) > 1:
            self.history.pop()
            self.students = copy.deepcopy(self.history[-1])
            self.save_data()
        else:
            raise ValueError
        
    def __load_file(self):
        try:
            if os.path.getsize(self.filename) > 0: 
                students = []
                line = ''
                with open(self.filename, "r")  as file:
                    line = file.readlines()
                for each in line:
                    line_splited = each.split(",")
                    students.append([copy.deepcopy(line_splited[0].strip()),copy.deepcopy(line_splited[1].strip()),copy.deepcopy(line_splited[2].strip())])
                for each in students:
                    self.add_student(Student(int(each[0]),each[1],int(each[2])))
        except FileNotFoundError:
            raise ("File not found.")
        except OSError:
            raise ("Cannot start repository")


class PickleRepository:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.history = [self.students]
        self.load_data()
        super().__init__()

    def load_data(self):
        try:
            with open(self.filename, 'rb') as file:
                students = []
                students = pickle.load(file)
                for each in students:
                    self.add_student(each)
        except FileNotFoundError:
            pass
    
    def save_data(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.students, file)

    def add_student(self, student):
        self.students.append(student)
        self.history.append(copy.deepcopy(self.students))
        self.save_data()

    def delete_students_in_group(self, group):
        self.students = [student for student in self.students if student.group != group]
        self.history.append(copy.deepcopy(self.students))
        self.save_data()

    def get_students(self):
        return self.students

    def undo_last_operation(self):
        if len(self.history) > 1:
            self.history.pop()
            self.students = copy.deepcopy(self.history[-1])
            self.save_data()
        else:
            raise ValueError
    
    
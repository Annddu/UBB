class Student:
    def __init__(self, student_id, name, group):
        self.student_id = student_id
        self.name = name
        self.group = group

    def serialize(self):
        return {"stundent_id": self.student_id,
                "name": self.name,
                "group": self.group}
    
    def __repr__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Group: {self.group})"
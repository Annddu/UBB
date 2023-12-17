class UI:
    def __init__(self, services):
        self.services = services

    def print_menu(self):
        print("\nMenu:")
        print("1. Add a student")
        print("2. Display the list of students")
        print("3. Filter students by group")
        print("4. Undo last operation")
        print("5. Exit")
    
    def get_ID(self):
        student_id = int(input("Enter student ID: "))
        if student_id.is_integer() == False:
            raise ValueError
        while self.services.verify_student_id(student_id) == True:
            print("Student ID already exists! Please try again.")
            student_id = int(input("Enter student ID: "))
            if student_id.is_integer() == False:
                raise ValueError
        return student_id
    
    def get_NAME(self):
        name = input("Enter student name: ")
        if name.isalpha() == False:
            raise ValueError
        return name
    
    def get_GROUP(self):
        group = int(input("Enter student group: "))
        if group.is_integer() == False or group < 0:
            raise ValueError
        return group
    
    def run(self):
        while True:
            self.print_menu()
          
            choice = input("Enter your choice: ")   
            
            try:
                if choice == '5':
                    print("Exiting...")
                    break
                
                elif choice == '1':
                    ok = False
                    while ok == False:
                        try:
                            student_id = self.get_ID()
                        except ValueError:
                            print("The ID should be an integer!")
                        else:
                            ok = True
                    
                    ok = False
                    while ok == False:
                        try:
                            name = self.get_NAME()
                        except ValueError:
                            print("The name should be a string!")
                        else:
                            ok = True    
                    
                    ok = False
                    while ok == False:
                        try:
                            group = self.get_GROUP()
                        except ValueError:
                            print("The group should be a positive integer!")
                        else:
                            ok = True
                            
                    self.services.add_student(student_id, name, group)
                    
                elif choice == '2':
                    print("List of students:")
                    self.services.display_students()
                    
                elif choice == '3':
                    try:
                        group = int(input("Enter group to filter: "))
                        if group < 0:
                            raise ValueError
                        while self.services.verify_student_group(group) == False:
                            print("Group does not exist! Please try again.")
                            group = int(input("Enter group to filter: "))
                            if group < 0:
                                raise ValueError
                    except ValueError:
                        print("The group should be a positive integer!")
                    self.services.filter_students_by_group(group)
                    
                elif choice == '4':
                    print("Undoing last operation...")
                    try:
                        self.services.undo_last_operation()
                    except ValueError:
                        print("No more operations to undo!")
                
            except ValueError:
                print("Please enter a valid value/command!")

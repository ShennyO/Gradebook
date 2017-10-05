from student import Student


class Class(object):
    """docstring for Class."""
    def __init__(self, name):
        # super(Class, self).__init__()
        self.name = name
        self.students = {}

    def create_student(self, name):
        temp_student = Student(name)
        self.students[name] = temp_student


    def delete_student(self, name):
        if self.students[name] in self.students:
            self.students.pop(name)


# history_class = Class("history")
# history_class.create_student("Sunny")
# history_class.students["Sunny"].add_assignment("homework1")
# history_class.students["Sunny"].update_assignment("homework1", 90)
# history_class.students["Sunny"].add_assignment("homework2")
# history_class.students["Sunny"].update_assignment("homework2", 90)
# print(history_class.students["Sunny"].assignments)
#
# history_class.students["Sunny"].remove_assignment("homework1")
# print(history_class.students["Sunny"].assignments)
#
# print(history_class.name)
# print(history_class.students["Sunny"].name)

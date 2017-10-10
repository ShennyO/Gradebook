from classroom import Classroom
from student import Student

# this is the function we call after we set up our classroom
def classroom_actions(Classroom):
    action = input("Hi! Welcome to your new classroom! Here are some of your actions for your classroom:(addStu - adds a new student to your classroom, remStu - removes named student from class, getStu - enter student account for further student actions: )")
    if action == "addStu":
        student_name = input("What is the name of your new student: ")
        new_student = Student(student_name)
        Classroom.students[student_name] = new_student
        print("Nice! You added %s to your %s classroom" % (student_name, Classroom))


def create_class(class_dict):
    name_of_class = input("Let's create a new classroom, What's the name of your class: ")
    day_class = input("What day/days does your class meet: ")
    time_class = input("What time does your class meet: ")
    new_class = Classroom(name_of_class, day_class, time_class)
    class_dict[name_of_class] = new_class
    print("Congratulations! You created %s class that meets %s at %s" % (name_of_class, day_class, time_class))



def main():
    classes_list = {}
    create_class(classes_list)
    print(classes_list)

main()

from classroom import Classroom, from student import Student

# this is the function we call after we set up our classroom
def classroom_actions():
    Input("Hi! Welcome to your new classroom! Here are your list of commands: ()")
    print()


def create_class():
    name_of_class = Input("Let's create a new classroom, What's the name of your class: ")
    day_class = Input("What day/days does your class meet: ")
    time_class = Input("What time does your class meet: ")
    new_class = Classroom(name_of_class, day_class, time_class)

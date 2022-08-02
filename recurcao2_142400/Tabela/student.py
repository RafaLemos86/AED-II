class Student:
    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

    def __repr__(self):
        return 'name: ' + str(self.name) + ' age: ' + str(self.age) + ' course: ' + str(self.course)

    def __str__(self):
        return 'name: ' + str(self.name) + ' age: ' + str(self.age) + ' course: ' + str(self.course)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return self.course

    def set_id(self, id):
        self.id = id

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_course(self, course):
        self.course = course

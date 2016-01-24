class UniversityPerson:
    pass
        
class Student(UniversityPerson):
    def __init__(self, schedule):
        self._schedule = schedule

    def addToSchedule(self, course):
        self._schedule.add_course(course)

class Professor(UniversityPerson):
    def __init__(self, schedule):
        self._schedule = schedule

class StaffPerson(UniversityPerson):
    def __init__(self, salary):
        self._salary = salary

class Registrar(StaffPerson):
    def __init__(self, schedule):
        self._schedule = schedule
    
    def addCourse(self, course):
        self._schedule.add_course(course)

    def removeCourse(self, course):
        self._schedule.remove_course(course)

class Schedule:
    def __init__(self, courses):
        self._courses = courses

    def add_course(self, course):
        self._courses.append(course)
    
    def remove_course(self, course):
        for i in self._courses:
            if i.getName() == course.getName():
                self._courses.remove(i)

    def display(self):
        for i in range(len(self._courses)):
            print(self._courses[i].getName(),  self._courses[i].getHour())
            

class Course:
    def __init__(self, hour, name):
        self._hour = hour
        self._name = name

    def getName(self):
        return self._name

    def getHour(self):
        return self._hour

def main():
    
    my_classes = [Course(3, 'B'), Course(5, 'D')]
    s = Schedule(my_classes)
    print("---------Original Schedule----------")
    print(s.display())
    s.add_course(Course(9, 'P'))
    print("---------Schedule After Adding One Class----------")
    print(s.display())
    s.remove_course(Course(3, 'B'))
    print("---------Schedule After Removing One Class----------")
    print(s.display())
    r = Student(s)
    print("---------Student's Schedule--------")
    print(s.display())
    r.addToSchedule(Course(11, 'MATH 301'))
    print("---------Student's Schedule After Adding a class---------")
    print(s.display())
    f = Professor(s)
    print("---------Professor's Schedule--------")
    print(s.display())
    y = Registrar(s)
    print("---------Registrar's Schedule--------")
    print(s.display())
    y.addCourse(Course(12, 'ECE 380'))
    print("---------Registrar's Schedule after adding a class---------")
    print(s.display())
    y.removeCourse(Course(12, 'ECE 380'))
    print("---------Registrar's Schedule after removing a class---------")
    print(s.display())

    
    

main()    

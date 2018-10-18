class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

    def eat(self,food):
        print("{} will eat {}".format(self,food))

class Student(Person):
    def __init__(self, firstname, lastname, school=""):
        super().__init__(firstname,lastname)
        self.school = school

    def __str__(self):
        return "{},[{}]".format(super().__str__(),self.school)

    def enroll (self):
        print("will enroll at {}".format(self.school))

if __name__ == "__main__":
        a = Person("JM","Portuguez")
        print(a)
        a.eat("eggs")

        jessie = Student("Jessie","Mendiola","ADNU")
        print(jessie)
        jessie.enroll()

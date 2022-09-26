from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def calc_age(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)

    def show(self):
        print(self.name +"'s age is: "+str(self.age))


mohan = Student("Mohan", 25)
mohan.show()

hari = Student.calc_age("Ram", 1980)
hari.show()
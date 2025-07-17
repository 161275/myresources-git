class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        total = 0
        for val in self.marks:
            total += val
        return(total/3)

s1 = Student("nish", [80, 95, 95])
print("The average marks of ", s1.name, " is ", s1.average())

s1.name = "ketan"     # changing or manipulating the values of attributes 
print("The average marks of ", s1.name, " is ", s1.average())


####Property decorator
class Student2:
    def __init__(self, name, phy, chem, math):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math

    # @property                         ##Property decorator
    @property
    def averag(self):
        avg = str((self.phy + self.chem + self.math) / 3) + "%"
        print(avg)

s2 = Student2("b", 90, 90, 90)
s2.averag()
s2.phy = 80

# s2.average()



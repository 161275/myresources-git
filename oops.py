class Student:                #class Student
    # def __init__(self):     #default constructor
    #    pass
    college = "JUIT"
    name = "xxxx"
    @staticmethod               #decorator
    def hello():                #static Mathod and operate at class level but dont have access to neither class attributrs nor object attributes
        print("HEllo World!")

    @classmethod
    def change_clg_name(cls, clg):
        cls.college = clg
    def __init__(self, name, marks, clg):    #parameterised constructor
        Student.college = clg                #changes the class attributes
        self.__class__.college = clg         #anothe way to change the class attribute. or else better method is to use @classmethod decorator
        print(self)
        self.name = name
        self.marks = marks
        print("adding new student")
    def  welcome(self):                  #Method
        print("welcome ", self.name)
    def get_marks(self):                 #Method
        return(self.marks)

s1 = Student("nishchal", 97, "JIIT")                #Object s1
print(s1)
print(s1.name, s1.marks)
print(Student.name)
s1.welcome()
print(s1.get_marks())
print(s1.college)
s1.change_clg_name("JUIT")
print(s1.college)


#operator Overloading
print(1 + 2) 
print(type(1))          #1 and 2 are objects of integer class
print("apna" + "college")
print(type("apna"))      #"apna" is object of string class
print([1,2,3] + [4,5,6])
print(type([1,2,3]))      #similarly list class
#In all three different classes + operator has different meaning(polymorphism)
#but this was implicit pollymorphism
#but similarly we can explicit in our classes


##constructor __init__function and automatically invokes when create an onject
##wheather we define it or not(python automatically create)

# Attributes can be class attributes and instance(object) attributes
# eg college is a class attribute andm name and marks are object attributes.
# object attributes have higher precedence than class attributes (in case same attribute name)

# Methos are function in the class and called by objects.


#Pillers of OOPs
# Abstraction => Hiding the implementation details of a class and only showing the essential features to the user
# Encapsulation => wrapping data and functions into a single unit(object)
# Inheritance => child or derived class Inherit he attributes and methods of Parent or base class
#                 single Inheritance => one parent and one child class
#                 multi-level Inheritance => class1 inherited by class2 inherited by class3 and so the last class also have also access to methods and attributes inherited by parent class
#                 multiple inheritance => child class inherit multiple base classes
# Polymorphism

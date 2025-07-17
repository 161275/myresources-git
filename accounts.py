class Accounts:
    ini_acc = '3420256'
    i = 1
    def print_bal(self):
        print(self.bal)
        print("Balance: " , self.bal)
    def __init__(self, in_dep, passwd):
        self.ac_number = Accounts.ini_acc + str(Accounts.i)
        self.bal = in_dep
        self.__passwd = passwd      #creating and mapping to private attribute that cloud be accessible only with in class not o/s of it
        Accounts.i += 1             #by adding __in the starting of attribute
        print(__passwd)             #similarly we can restrict the scope of method by ading __ before method name.
        print("your acount number is: ", self.ac_number)
    def credit(self, amt):
        self.bal += amt
        print("Rs.", amt, "was credited \nUpdated Bal: " , self.bal)
    def debit(self, amt):
        self.bal -= amt
        print("Rs.", amt, "was debited \nUpdated Bal: " , self.bal)

c1 = Accounts(10000, 'User@Password')
c1.debit(500)
c1.credit(20000)
# print(c1.__passwd)    cause an error because a private attribute.
del c1.ac_number.       #deleting ac_number attribute of c1 object
c1.print_bal()
del c1                  #deleting entire c1 object
c1.print_bal()
c2 = Accounts(2000)




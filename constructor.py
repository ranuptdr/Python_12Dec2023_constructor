# 1. class Defination
class Parent():
    #1.1 Property = Value
    bloodGroup = '' #Define Property

    #1.2 constructor is a special Function/Method
    def __init__(self):
        self.bloodGroup = 'A+ve' # Property value initialization
        pass

    #1.3 Method = Function 
    def myMethod(self):
        print(f'My Blood Group is {self.bloodGroup}')
    pass

# 2. create class object
ceo = Parent()

#2.1  call the Method With Class Object
ceo.myMethod()
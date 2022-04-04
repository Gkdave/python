class Employee:

    def __init__(self, id ,name, role, Salary):
        self.id = id
        self.name = name
        self.role = role
        self.salary = Salary
    def disp(self):
        print( f"the id is {self.id} and the name is {self.name} the role is {self.role} and salary is {self.salary}")


emp=Employee('1','gajendra','teacher',23000) 
emp1=Employee('2','Ravi','teacher',30000)
emp1.disp() 
emp.disp() 
    

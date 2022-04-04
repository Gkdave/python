#stu.py
class Student:
    no_of_leave = 15
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address

    def disp(self, s):
        self.styfund = s

        print(f'The Name is : {self.name } and  Roll: {self.roll }  and  Address: {self.address} and styfund is {self.styfund}.')

himanshu=Student('himanshu',11,'udaipur')
himanshu.disp(3000)
# Student.no_of_leave = 20
# print(himanshu.no_of_leave)









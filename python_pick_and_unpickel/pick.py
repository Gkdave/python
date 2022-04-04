# pick.py
# Storeing Object in the file


# import pickle
# class Student:
#     def __init__(self, name, roll, address):
#         self.name = name
#         self.roll = roll
#         self.address = address
#     def disp(self):
#         print(f'Name: {self.name} Roll: {self.roll} address: {self.address}')
#
# with open('student.dat', mode='wb')as f:
#     stu1 = Student('rahul',101,'Rachi')
#     stu2 = Student('Sonam',102,'Dhanbad')
#     pickle.dump(stu1, f)
#     pickle.dump(stu2, f)
#     print('Pickling Done')
#
#
# with open('student.dat',mode='rb') as f:
#     obj1 = pickle.load(f)
#     obj2 = pickle.load(f)
#     print('unpicklong')
#     obj1.disp()
#     obj2.disp()
#








import pickle, stu
n = int(input('Enter Number of Students:  '))
with open('student.dat', mode= 'wb')as f:
    for i in range(n):
        name = input("Enter Student Name:  ")
        roll = int(input("Enter Roll:  "))
        address = input('Enter Address :  ')
        stu1 = stu.Student(name, roll, address)
        pickle.dump(stu1, f)

print('Pickling Done!!!')
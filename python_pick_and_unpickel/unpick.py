# Unpick.py
#Reading Object from the file

import pickle

# with open('student.dat', mode='rb') as f:
#     while True:
#         try:
#             obj = pickle.load(f)
#             obj.disp()
#         except EOFError:
#             print('Done')
#             break

with open('student.dat', mode='rb') as f:
    while True:
        try:
            obj = pickle.load(f)
            obj.disp()

        except EOFError:
            print('Done')
            break


# from shutil import copyfile
# copyfile('student.dat', 'student.txt')
# f = open('student.txt', mode='r')
# print(f.read())
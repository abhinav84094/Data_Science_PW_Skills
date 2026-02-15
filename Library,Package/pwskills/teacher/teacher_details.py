import os, sys
from os.path import dirname, join, abspath

parent_dir_path = abspath(join(dirname(__file__), ".."))
print(parent_dir_path)

sys.path.insert(0, parent_dir_path)


from student import student_details

student_details.student()


def teacher():
    print("This is teacher details...")


teacher()

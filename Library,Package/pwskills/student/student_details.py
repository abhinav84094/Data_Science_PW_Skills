import os, sys  # os provide functionality to interact with os ans sys provides access to system specific parammeters and function such as python path
from os.path import dirname, join, abspath

parent_dir_path = abspath(join(dirname(__file__),".."))
sys.path.insert(0, parent_dir_path)  # at index 0 add this directory



def student():
    print("This is student detials...")

student()



from teacher import teacher_details # import teacher_details from teacher package

teacher_details.teacher()
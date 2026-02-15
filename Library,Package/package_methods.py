import os, sys  # os provide functionality to interact with os ans sys provides access to system specific parammeters and function such as python path
from os.path import dirname, join, abspath

print("Full path of this file : ", __file__) # this will give path to current script

print("Directory name : ", dirname(__file__)) # give the directory containing the current script

print(join(dirname(__file__), "..")) # just combines this and give now path

print(abspath(join(dirname(__file__), ".."))) # abspath will give absolute path after joining 
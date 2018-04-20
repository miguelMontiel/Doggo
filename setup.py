import os
import cx_Freeze
from cx_Freeze import *

os.environ['TCL_LIBRARY'] = r'C:\Users\IBM_ADMIN\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\IBM_ADMIN\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(
    name = "Doggo",
    options = {'build_exe': {'packages': ['pygame', 'pytmx']}},
    executables = [Executable('Main.py')]
)
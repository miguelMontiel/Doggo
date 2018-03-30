import cx_Freeze
from cx_Freeze import *

setup(
    name = "Doggo",
    options = {'build_exe': {'packages': ['pygame', 'pytmx']}},
    exec = [
        Executable(
            'Main.py'
        )
    ]
)
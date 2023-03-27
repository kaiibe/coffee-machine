import os
import platform

def clear_terminal():
    print(platform.system())
    if platform.system() == "Darwin":
        os.system("clear") 
    else:
        os.system("cls") 
'''
Created on 16 sept. 2018

@author: Swann
'''

import subprocess
import sys

def install(package, path = sys.executable):
    return subprocess.call([path, "-m", "pip", "install", package])
    
if __name__ == '__main__':
    list_package = ["pygame", "screeninfo"]
    for package in list_package:
        if (install(package) != 0):
            path = input("Please tap the absolute path of your python location:")
            if (install(package, path) != 0):
                print("Failure... Try in your cmd:")
                print("python -m pip install", package)
    input()
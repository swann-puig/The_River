'''
Created on 16 sept. 2018

@author: Swann
'''

import subprocess
import sys
import os

def install(package, path = sys.executable):
    return subprocess.call([path, "-m", "pip", "install", package])
    
if __name__ == '__main__':
    list_package = ["pygame", "screeninfo"]

    try: # see if pip is installed
        subprocess.call([sys.executable, "-V"])
        subprocess.call([sys.executable, "-m", "pip", "-V"])
    except:
        if (os.name != 'nt'):
            if (subprocess.call(["curl", "https://bootstrap.pypa.io/get-pip.py", "-o", "get-pip.py"]) != 0):
                print("Failure... Try in your cmd:")
                print("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
            if (subprocess.call([sys.executable, "get-pip.py"]) != 0):
                print("Failure... Try in your cmd:")
                print("python get-pip.py")
        else:
            print("Install Python 3.5+ or add Python in your environment PATH.")
            
    for package in list_package:
        if (install(package) != 0):
                print("Failure... Try in your cmd:")
                print("python -m pip install", package)
                
    input("Finished")
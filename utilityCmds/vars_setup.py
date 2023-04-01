import files
import inspect
import os

def newPath(path,fileName):
    path = os.path.join(path,fileName)
    return path
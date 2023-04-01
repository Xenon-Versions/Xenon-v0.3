import funcs
import os

def files():
    try:
        dir_path = os.getcwd()
        files = os.listdir(dir_path)
        print(f"Total files: {len(files)}")
        cnt = 0
        while cnt != len(files):
            print(f"[File number:{cnt}]: {files[cnt]}")
            cnt = cnt+1
    except PermissionError:
        funcs.printAndSay("Access denied")
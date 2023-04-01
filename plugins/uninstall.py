import os

def uninstallXenon():
    try:
        os.rmdir(f"C:/Users/{os.getlogin()}/Xenon")
    except:
        pass
    try:
        os.remove(f"C:/Users/{os.getlogin()}/Desktop/Xenon.bat")
    except:
        pass
    try:
        os.remove(f"C:/Users/{os.getlogin()}/AppData/Local/Microsoft/WindowsApps/")
    except:
        pass
    try:
        os.remove(f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
    except:
        pass
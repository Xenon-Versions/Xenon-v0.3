import os
import traceback
os.system("title Please wait...")
os.chdir(f"C:/Users/{os.getlogin()}")

try:
    import worker
    import itsXenon

    dataBase = open(worker.newPath(worker.dataBasePath,"xenonConfig.XE"),"rb")
    itsXenon.qLoop()
except Exception as e:
    #traceback.print_exc()
    worker.varset()
    import itsXenon
    itsXenon.qLoop()

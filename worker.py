import pickle
import os
import inspect
import help

def newPath(path, fileName):
    path = os.path.join(path, fileName)
    return path

pathX = newPath("C:/Users", str(os.getlogin()))
itsXenonPath = inspect.getfile(help)
itsXenonPath = os.path.join(pathX, itsXenonPath)

xenonPath = itsXenonPath.replace("help.py", "")
dataBasePath = os.path.join(xenonPath, "xenonData")

def varset():
    file = open(newPath(dataBasePath, "xenonConfig.XE"), "w")
    file.close()
    name = input("Enter your name:")
    title = input("Enter window title: ")
    speech = input("Enetr speech status[on/off]: ")
    city = input("Enetr your city name: ")
    data = {}
    data["name"] = name
    data["title"] = title
    data["speech"] = speech
    data["city"] = city
    file = open(newPath(dataBasePath, "xenonConfig.XE"), "wb")
    pickle.dump(data, file)
    file.close()
    try:
        file = open(newPath(dataBasePath,"records.XE"),"rb")
    except:
        record = {}
        file = open(newPath(dataBasePath,"records.XE"),"wb")
        pickle.dump(record,file)



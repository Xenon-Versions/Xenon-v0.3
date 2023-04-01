import os
import funcs
import Levenshtein
import inspect


def chage(user):
    userS = user.split(" ")
    try:
        num = int(userS[1])
        path = os.getcwd()
        listFiles = os.listdir(path)
        os.chdir(listFiles[num])
        funcs.printAndSay(f"Path changed to: {os.getcwd()}")
    except:
        os.chdir(user[3:])
        os.chdir(listFiles[num])
        funcs.printAndSay(f"Path changed to: {os.getcwd()}")
def back():
    os.chdir("..")

def find(user):
    print()
    userS = user.split(" ")
    subCommand = userS[1]
    root = f"C:/Users/{os.getlogin()}"
    if subCommand == "-folder":
        funcs.printAndSay("Please wait")
        folderName = user[(6 + len(subCommand)):]
        folders = []
        for a, b, c in os.walk(root):
            spliting = a.split("\\")
            file = spliting[-1]
            if file == folderName:
                folders.append(a)
        if len(folders) == 1:
            funcs.printAndSay("Found 1 result:")
        else:
            funcs.printAndSay(f"Found {len(folders)} results:")
        cnt = 0
        while cnt != len(folders):
            print(f"[{cnt+1}]:{folders[cnt]}")
            os.startfile(folders[cnt])
            cnt += 1
        #advanced search
        if len(folders) == 0:
            foldDict = {}
            funcs.printAndSay("Lite search failed. Starting advanced search")
            for a,b,c in os.walk(root):
                spliting = a.split("\\")
                folder = f'{spliting[-1]}'
                distance = Levenshtein.distance(folderName,folder)
                foldDict[a] = distance
            lisCreat = list(foldDict.values())
            enum_lst = list(enumerate(lisCreat))
            sorted_lst = sorted(enum_lst, key=lambda x: x[1])[:50]
            goldList = []
            for i, val in sorted_lst:
                goldList.append(i)
            listF = list(foldDict.keys())
            cnt = 0
            while cnt != 10:
                print(f"[{cnt}]: {listF[goldList[cnt]]}")
                os.startfile(listF[goldList[cnt]])
                cnt += 1
        print()
    if subCommand == "-file":
        fileName = user[(6+len(subCommand)):]
        files = []
        for a,b,c in os.walk(root):
            cnt = 0
            while cnt != len(c):
                if c[cnt] == fileName:
                    files.append(str(os.path.join(a,c[cnt])))
                cnt += 1
        if len(files) == 1:
            funcs.printAndSay("Found 1 result:")
        else:
            funcs.printAndSay(f"Found {len(files)} results:")
        cnt = 0
        while cnt != len(files):
            print(f"[{cnt+1}]: {files[cnt]}")
            os.startfie(files[cnt])
            cnt += 1
        print()
        if len(files) == 0:
            print("Starting advanced search")
            fileDict = {}
            for a,b,c in os.walk(root):
                cnt = 0
                while cnt != len(c):
                    distance = Levenshtein.distance(fileName,c[cnt])
                    fileDict[os.path.join(a,c[cnt])] = distance
                    cnt += 1
            lisCreat = list(fileDict.values())
            enum_lst = list(enumerate(lisCreat))
            sorted_lst = sorted(enum_lst, key=lambda x: x[1])[:50]
            goldList = []
            for i, val in sorted_lst:
                goldList.append(i)
            listF = list(fileDict.keys())
            cnt = 0
            while cnt != 10:
                print(f"[{cnt}]: {listF[goldList[cnt]]}")
                os.startfile(listF[goldList[cnt]])
                cnt += 1




def fHandeler(user):
    subCommand = user.split(" ")[1]
    #creation
    if subCommand == "-make-file":
        path = user[(6+len(subCommand)):]
        with open(path,"w") as f:
            funcs.printAndSay(f"File successfully created at {path}")
            os.startfile(path)
    if subCommand == "-make-folder":
        path = user[(6+len(subCommand)):]
        os.mkdir(path)
        funcs.printAndSay(f"Folder successfully created at {path}")
        os.startfile(path)
    #deletation
    if subCommand == "-del-file":
        path = user[(6+len(subCommand)):]
        os.remove(path)
        funcs.printAndSay("File successfully removed")
    if subCommand == "-del-folder":
        path = user[(6+len(subCommand)):]
        os.rmdir(path)
        funcs.printAndSay("Folder successfully removed")


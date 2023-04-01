import os
import vars_setup
def view(user):
    path = os.getcwd()
    files = os.listdir(path)
    userS = user.split(" ")
    try:
        dicNum = int(userS[1])
        file = vars_setup.newPath(path,files[dicNum])
        os.startfile(file)
    except:
        path = os.getcwd()
        file = user[5:]
        os.startfile(vars_setup.newPath(path,file))
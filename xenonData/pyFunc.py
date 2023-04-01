import myInfo
import os
import inspect

file = inspect.getfile(myInfo)
path = file.replace("myInfo.py","")

def getTempData():
    file = open(f"{os.path.join(path,'tempdata.tem')}","r")
    data = file.read()
    return data

def saveTempData(data):
    file = open(f"{os.path.join(path,'tempdata.tem')}","w")
    file.write(data)

def alert(title,message):
    import tkinter

    wn = tkinter.Tk()
    wn.geometry("300x100")
    wn.title(title)

    text = tkinter.Label(
        wn,
        text=message,
        pady=25
    )
    close = tkinter.Button(
        wn,
        text="Close",
        command=wn.destroy,
        height=1,
        width=10
    )

    text.pack()
    close.pack()

    wn.mainloop()
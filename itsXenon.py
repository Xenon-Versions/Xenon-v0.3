import os
import traceback
import vars_setup


def install(module):
    os.system("cls")
    print(f"Installing: {module}")
    os.system(f"pip install {module}")


def installImports():
    install("pyperclip")
    install("pyautogui")
    install("comtypes")
    install("wikipedia")
    install("opencv-python")
    install("python-open-weather")
    install("pycaw")
    install("PyPI-Browser")
    install("requests")
    install("inspect")
    install("openai")
    install("calendar")
    install("plyer")
    install("pyttsx3")
    install("phonenumbers")
    install("psutil")
    install("art")
    install("pillow")


try:
    import webbrowser as webb
    import psutil
    import art
    import phonenumbers as pn
    import pyttsx3
    import help
    import ast
    import pickle
    import requests
    import openai
    import inspect
    import pyperclip
    import calendar
    import logging
    from xenonData import myInfo
    import pyautogui as gui
    import funcs
except Exception as e:
    installImports()
    print("[PLEASE RESTART]")
    quit()

from plugins import echo, \
    fexit, \
    send, \
    rma, \
    timer, \
    restart, \
    save, \
    web, \
    search, \
    ascii, \
    wiki, \
    exit, \
    system, \
    cal, \
    calculator, \
    imgfile, \
    server, \
    wifi, \
    files, \
    filesM, \
    trash, \
    ss, \
    windowHandler, \
    weatherHandling, \
    admin, \
    chatgpt, \
    FTPxenon, \
    uninstall

from utilityCmds import view, \
    clear, \
    internal


# exceptional commands

def helpCmd(user):
    userS = user.split(" ")
    if len(userS) == 1:
        print(
            f"Total commands: {len(xenonCmdsNoUser) + len(xenonCmdsUser) + len(utilityCmds) + len(utilityCmdsWithInput) + 2}")
        for i in help.helpCmd:
            print(f"\n-{1 + (list(help.helpCmd).index(i))}[{i}]: {help.helpCmd.get(i)}")
    else:
        cmdInfo = help.helpCmd.get(userS[1])
        if cmdInfo == None:
            print(f"{vars_setup.DevInfo.assistantName(passw=False)}:No such command")
        else:
            print(f"{userS[1]}: {cmdInfo}")


def aliasHandler(user):
    subCommand = user.split(" ")[1]
    if subCommand == "-add":
        aliasName = user.split(" ")[2]
        try:
            aliasWork = xenonCmdsUser[user[(12 + len(aliasName)):]]
            funcs.addAlias(aliasName, aliasWork, funcs.loadAlias())
            funcs.printAndSay(f"{aliasName} added")
        except:
            try:
                aliasWork = xenonCmdsNoUser[user[(12 + len(aliasName)):]]
                funcs.addAlias(aliasName, aliasWork, funcs.loadAlias())
                funcs.printAndSay(f"{aliasName} added")
            except:
                try:
                    aliasWork = utilityCmds[user[(12 + len(aliasName)):]]
                    funcs.addAlias(aliasName, aliasWork, funcs.loadAlias())
                    funcs.printAndSay(f"{aliasName} added")
                except:
                    aliasWork = xenonCmdsUser[user[(12 + len(aliasName)):]]
                    funcs.addAlias(aliasName, aliasWork, funcs.loadAlias())
                    funcs.printAndSay(f"{aliasName} added")
    if subCommand == "-ls":
        funcs.listAlias(funcs.loadAlias())
    if subCommand == "-del":
        try:
            aliasName = user.split(" ")[2]
            funcs.removeAlias(aliasName, funcs.loadAlias())
            funcs.printAndSay(f"{aliasName} removed")
        except:
            funcs.printAndSay(f"{user.split(' ')[2]} not found")
    if subCommand == "-reset":
        funcs.resetAlias(funcs.loadAlias())
        funcs.printAndSay("All alias removed")


try:
    user = vars_setup.Personal()
    os.system(f"title {user.title()} Loading...")
except:
    restart.restart(realtimeVars=True)

realtimeVars = {
    "running": True
}

xenonCmdsNoUser = {
    "clear": clear.clear,
    "video": trash.vidCap,
    "chatgpt": chatgpt.chatGPTloop,
    "exit": exit.leaveIt,
    "desk": trash.desk,
    "fexit": fexit.fexit,
    "pic": trash.photoCap,
    "c-server": server.close
}
xenonCmdsUser = {
    "web": web.web,
    "search": search.search,
    "find": filesM.find,
    "save": save.save,
    "internal": system.internal,
    "ftp": FTPxenon.ftpStart,
    "timer": timer.timer,
    "wifi": wifi.wifiHandler,
    "ss": ss.ssHandeler,
    "calc": calculator.calculator,
    "file": filesM.fHandeler,
    "wiki": wiki.wikiHandler,
    "uninstall": uninstall.uninstallXenon,
    "help": helpCmd,
    "weather": weatherHandling.weatherHandler,
    "desk": trash.desk,
    "launch": server.launch,
    "mirror": trash.mirror,
    "dp": imgfile.quickdp,
    "admin": admin.doAdmin,
    "cd": filesM.chage,
    "cal": cal.calY,
    "show": windowHandler.winHandler,
    "cls": windowHandler.winHandler,
    "max": windowHandler.winHandler,
    "mini": windowHandler.winHandler,
    "send": send.send,
    "echo": echo.echo,
    "reminder": rma.rma,
    "art": ascii.asciiHandler
}
utilityCmds = {
    "ls": files.files,
    "refresh": trash.startMsg,
    "goback": filesM.back,
    "his": system.his,
    "errors": system.errRep
}
utilityCmdsWithInput = {
    "view": view.view,
    "cmd": internal.commandRuner
}


def qLoop():
    print("Loading...")
    user = vars_setup.Personal()
    os.system(f"title {user.title()}")
    os.system("cls")
    try:
        print(vars_setup.Messages.startMsg(True))
    except Exception as e:
        print(e)
        print(vars_setup.Messages.startMsgNW(True))
    running = True
    while running:
        try:
            path = os.getcwd()
            us = vars_setup.Personal()
            user = input(f"{us.name()}[{path}]: ")
            file = open(vars_setup.newPath(vars_setup.dataBasePath, "history.txt"), "a")
            file.write(f"\n[{vars_setup.timeNow}]: {user}")
            file.close()
            userS = user.split(" ")
            if user in xenonCmdsNoUser:
                xenonCmdsNoUser[str(userS[0])]()
            if userS[0] in xenonCmdsUser:
                xenonCmdsUser[str(userS[0])](user)
            if userS[0] in utilityCmds:
                utilityCmds[str(userS[0])]()
            if userS[0] in utilityCmdsWithInput:
                utilityCmdsWithInput[str(userS[0])](user)
            if userS[0] == "restart":
                restart.restart(realtimeVars)
            if userS[0] == "alias":
                aliasHandler(user)
            if userS[0] == "reset":
                vars_setup.varset()
            if userS[0] == "reset-gpt-api":
                vars_setup.resetGptApi()
            file = open(vars_setup.newPath(vars_setup.dataBasePath, "alias.lock"), "rb")
            alias = pickle.load(file)
            if userS[0] == "admin-reset":
                vars_setup.reset_config()
                funcs.printAndSay("D0NE")
                restart.restart(realtimeVars)
            try:
                if userS[0] in alias:
                    alias[str(userS[0])](user.replace(userS[0], ""))
            except:
                alias[str(userS[0])]()
            try:
                result = eval(user)
                result = int(result)
                funcs.printAndSay(f"Your answer is {result}")
            except:
                pass
        except:
            file = open(vars_setup.newPath(vars_setup.dataBasePath, "error-report.txt"), "a")
            file.write(f"\nLatest Error occurred on {vars_setup.timeNow}:-")
            traceback.print_exc(file=file)
            file.close()

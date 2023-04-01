import echo
import inspect
import shutil
import os
import psutil
import datetime
import platform
from weather import Weather,celsius
import pickle
from weatherHandling import xenonWeather

def newPath(path,fileName):
    path = os.path.join(path,fileName)
    return path

def printCentre(s):
    its = s.split("\n")
    for i in its:
        "".join(i)
        print(i.center(shutil.get_terminal_size().columns))


pathX = os.path.join("C:/Users",os.getlogin())
itsXenonPath = inspect.getfile(echo)
xenonPath = itsXenonPath.replace("plugins/echo.py","")
xenonPath = os.path.join(pathX,xenonPath)
dataBasePath = os.path.join(xenonPath,"xenonData")
ssPath = os.path.join(dataBasePath,"Screen-Shots")
picPath = os.path.join(dataBasePath,"Photos")
rssPath = os.path.join(dataBasePath,"RSS")
bgPath = os.path.join(rssPath,"Backgrounds")
fontPath = os.path.join(rssPath,"Fonts")
logoPath = os.path.join(dataBasePath,"Logos")
catPath = os.path.join(dataBasePath,"Catlogs")


class Personal:
    file = open(newPath(dataBasePath, "xenonConfig.XE"), "rb")
    data = pickle.load(file)

    def name(self):
        name = self.data["name"]
        return name

    def title(self):
        title = self.data["title"]
        return title

    def speech(self):
        speech = self.data["speech"]
        return speech

    def city(self):
        city = self.data["city"]
        return city


timeNow = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}"


class Messages():
    def startMsg(passw):
        user = Personal()
        msg = f"""
->Welcome {user.name()}
->Program Name: {DevInfo.assistantName(passw)}
->Manager version: {DevInfo.version(passw)}
->Current time: {timeNow}
->System Battery: {DevInfo.getBattery(passw)}
->System: {DevInfo.deskSystem(passw)}
->Charging status: {DevInfo.isChargning(passw)}
->Processor: {DevInfo.processor(passw)}
->Python version: {DevInfo.pyVer(passw)}
->System bit: {DevInfo.sysBit(passw)}
->Weather: {DevInfo.weather(passw)}

Do 'help' to see command list
"""
        return msg

    def startMsgNW(passw):
        user = Personal()
        msg = f"""
->Welcome {user.name()}
->Program Name: {DevInfo.assistantName(passw)}
->Manager version: {DevInfo.version(passw)}
->Current time: {timeNow}
->System Battery: {DevInfo.getBattery(passw)}
->System: {DevInfo.deskSystem(passw)}
->Charging status: {DevInfo.isChargning(passw)}
->Processor: {DevInfo.processor(passw)}
->Python version: {DevInfo.pyVer(passw)}
->System bit: {DevInfo.sysBit(passw)}
->Weather : Cant load , Check your internet connection

Do 'help' to see command list
"""
        return msg

    def weatherMsg(city):
        msg = f"""
{printCentre("[WEATHER-REP0RT]")}
City: {xenonWeather.getCity(city)}
Temperature: {xenonWeather.getTemp(city)}
Pressure: {xenonWeather.getPressure(city)}
Humidity: {xenonWeather.getHumidity(city)} 
Description: {xenonWeather.getDescription(city)}

"""
        return msg


class DevInfo():
    def version(passw):
        ver = f"v[0.2]"
        return ver

    def assistantName(passw):
        name = "Xenon"
        return name

    def getBattery(passw):
        battery = psutil.sensors_battery().percent
        if psutil.sensors_battery().power_plugged:
            batteryP = f"↑ {battery}%"
        else:
            batteryP = f"{battery}%"
        return batteryP

    def isChargning(passw):
        isCharging = psutil.sensors_battery().power_plugged
        if isCharging == False:
            status = "Unpluged"
        else:
            status = "Pluged"
        return status

    def sysBit(passw):
        bit = platform.machine()
        bitS = bit.split("_")
        return str(bitS[0])

    def processor(passw):
        return str(platform.processor())

    def pyVer(passw):
        return str(platform.python_version())

    def deskSystem(passw):
        return str(platform.uname().system)

    def weather(passw):
        weather = Weather(temperature_unit=celsius)
        user = Personal()
        info = weather.fetch_weather(user.city())

        strToGive = f"\n==>City: {info['City: ']}\n==>Temprature: {info['Temperature: ']}\n==>Description: {info['Description: ']}"
        return strToGive

def varset():
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

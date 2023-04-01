from weather import Weather,celsius
import vars_setup
import funcs

weather = Weather(temperature_unit=celsius)


class xenonWeather():
    def getTemp(city):
        report = weather.fetch_weather(city)
        temp = report["Temperature: "]
        return temp

    def getCity(city):
        return city

    def getPressure(city):
        report = weather.fetch_weather(city)
        pressure = report["Pressure: "]
        return pressure

    def getHumidity(city):
        report = weather.fetch_weather(city)
        humidity = report["Humidity: "]
        return humidity

    def getDescription(city):
        report = weather.fetch_weather(city)
        description = report["Description: "]
        return description

def weatherHandler(user1):
    user = vars_setup.Personal()
    userS = user1.split(" ")
    if len(userS) == 1:
        funcs.printAndSay(vars_setup.Messages.weatherMsg(user.city()))
    subCommand = userS[1]
    if len(userS) == 2:
        if subCommand == "-temp":
            funcs.printAndSay(f"Temperature [{user.city()}] -  {xenonWeather.getTemp(user.city())}")
        if subCommand == "-pressure":
            funcs.printAndSay(f"Pressure [{user.city()}] - {xenonWeather.getPressure(user.city())}")
        if subCommand == "-humidity":
            funcs.printAndSay(f"Humidity [{user.city()}] - {xenonWeather.getHumidity(user.city())}")
        if subCommand == "-description":
            funcs.printAndSay(f"Short word to describe weather over there [{user.city()}] - {xenonWeather.getDescription(user.city())}")
        else:
            city = user[8:]
            funcs.printAndSay(vars_setup.Messages.weatherMsg(city))
    else:
        subCommand = userS[1]
        city = user[(9+len(subCommand)):]
        if subCommand == "-temp":
            funcs.printAndSay(f"Temperature [{city}] -  {xenonWeather.getTemp(city)}")
        if subCommand == "-pressure":
            funcs.printAndSay(f"Pressure [{city}] - {xenonWeather.getPressure(city)}")
        if subCommand == "-humidity":
            funcs.printAndSay(f"Humidity [{city}] - {xenonWeather.getHumidity(city)}")
        if subCommand == "-description":
            funcs.printAndSay(f"Short word to describe weather over there [{city}] - {xenonWeather.getDescription(city)}")
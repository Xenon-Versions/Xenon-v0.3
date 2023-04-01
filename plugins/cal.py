import calendar
from datetime import datetime as dt
import funcs

def calY(user):
    userS = user.split(" ")
    if len(userS) == 1:
        year = dt.now().year
        print(calendar.calendar(year))
    else:
        if len(userS) == 2:
            try:
                year = int(userS[1])
                print(calendar.calendar(year))
            except:
                funcs.printAndSay("Something went wrong")
        else:
            try:
                year = int(userS[1])
                month = int(userS[2])
                print(calendar.month(year,month))
            except:
                funcs.printAndSay("Something went wrong!")
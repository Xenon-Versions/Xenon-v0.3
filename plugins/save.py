import funcs
import vars_setup
def save(user):
    funcs.printAndSay("Your note has been saved")
    userS = user.split(" ")
    file = open(vars_setup.newPath(vars_setup.dataBasePath,f"{userS[1]}.txt"),"w")
    text = user.replace(f"save {userS[1]}","")
    file.write(text)

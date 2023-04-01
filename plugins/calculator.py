import funcs

def calculator(user):
    userS = user.split(" ")
    expression = userS[1]
    expression = expression.replace("x","*")
    expression = expression.replace("%","/")
    try:
        funcs.printAndSay(f"Your answer is {eval(expression)}")
    except:
        funcs.printAndSay("Something went wrong\n~Not a correct mathematical expression")
import webbrowser as webb
def web(user):
    link = user.replace("web","")
    superLink = f"https://{link}"
    webb.open(superLink)

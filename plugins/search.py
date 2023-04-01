import webbrowser as webb
def search(user):
    toSearch = user.replace("search","")
    link = f"https://www.google.com/search?q=hi&rlz=1C1RXQR_enIN1036IN1036&oq={toSearch}&aqs=chrome..69i57j69i60l3.900j0j7&sourceid=chrome&ie=UTF-8"
    webb.open(link)

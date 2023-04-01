import wikipedia

def wikiHandler(user):
    print("[Please Wait]")
    text = user.replace("wiki","")
    searches = wikipedia.search(text)
    cnt = 0
    while cnt != len(searches):
        print(f"[{cnt}]: {searches[cnt]}")
        cnt += 1
    try:
        num = int(input(f"Enter desired search number[0/{len(searches)-1}]: "))
        result = wikipedia.summary(searches[num])
        print(result)
    except:
        print("Error: Enter a number")
import openai
import vars_setup
import pickle
import funcs
import webbrowser as web



def chatGPTloop():
    try:
        file = open(vars_setup.newPath(vars_setup.dataBasePath, "gptapi.XE"), "rb")
        file.close()
    except:
        funcs.printAndSay("Get API_KEY from https://platform.openai.com/account/api-keys")
        web.open("https://platform.openai.com/account/api-keys")
        gptapi = input("Enter API_KEY: ")
        api = {}
        api["chatgpt"] = gptapi
        file = open(vars_setup.newPath(vars_setup.dataBasePath, "gptapi.XE"), "wb")
        pickle.dump(api, file)
        file.close()

    file = open(vars_setup.newPath(vars_setup.dataBasePath, "gptapi.XE"), "rb")
    api = pickle.load(file)
    gptapi = api["chatgpt"]
    openai.api_key = gptapi

    def getResponse(message):
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = chat_completion.choices[0].message.content
        return answer

    funcs.printAndSay("Type exit to go back to Xenon Loop")
    gptRun = True
    while gptRun:
        user = input("You: ")
        if user == "exit":
            gptRun = False
        response = getResponse(message=user)
        funcs.printAndSayGPT(response)

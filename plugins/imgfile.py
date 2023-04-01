from PIL import Image, ImageDraw, ImageFont
import vars_setup
import funcs
import random
import os

colors = [
    (255,41,76),(255,199,41),
    (0,200,255),(21,255,160),
    (120,255,91),(255,3,81),
    (142,144,255)
]

def quickdp(user):
    userS = user.split(" ")
    bgPathList = os.listdir(vars_setup.bgPath)
    fontPath = os.listdir(vars_setup.fontPath)
    background = vars_setup.newPath(vars_setup.bgPath,random.choice(bgPathList))
    font = vars_setup.newPath(vars_setup.fontPath,random.choice(fontPath))
    subcommand = user.split(" ")[1]
    if len(userS) == 2:
        inputStr = user[3:]
        img = Image.open(background)
        draw = ImageDraw.Draw(img)
        fontf = ImageFont.truetype(font, 150)
        textS = inputStr.split(" ")
        if len(textS) > 10:
            funcs.printAndSay("Word limit reached [10]")
            raise TypeError("Word limit reached")
        text = "\n".join(textS)
        textwidth, textheight = draw.textsize(text, fontf)
        x = (img.size[0] - textwidth) / 2
        y = (img.size[1] - textheight) / 2
        draw.text((x, y), text, font=fontf, fill=random.choice(colors))
        filenum = funcs.getNum(3)
        img.save(vars_setup.newPath(vars_setup.dataBasePath,vars_setup.newPath(vars_setup.logoPath,f"Logo-{filenum}.png")))
        os.startfile(vars_setup.newPath(vars_setup.logoPath,f"Logo-{filenum}.png"))
    if subcommand == "-catlog":
        funcs.printAndSay("Please Wait...")
        nImagesStr = user.split(" ")[2]
        nImages = int(nImagesStr)+1
        funcs.printAndSay(f"Making new catlog with {nImagesStr} images")
        inputStr = user[(4+len(subcommand)+len(nImagesStr)):]
        n = 1
        filenum = funcs.getNum()
        os.mkdir(vars_setup.newPath(vars_setup.catPath,f"Catlog-{filenum}"))

        newCatPath = vars_setup.newPath(vars_setup.catPath,f"Catlog-{filenum}")
        while n != nImages:
            bgPathList = os.listdir(vars_setup.bgPath)
            fontPath = os.listdir(vars_setup.fontPath)
            background = vars_setup.newPath(vars_setup.bgPath, random.choice(bgPathList))
            font = vars_setup.newPath(vars_setup.fontPath, random.choice(fontPath))
            img = Image.open(background)
            draw = ImageDraw.Draw(img)
            fontf = ImageFont.truetype(font, 150)
            textS = inputStr.split(" ")
            if len(textS) > 10:
                funcs.printAndSay("Word limit reached [10]")
                raise TypeError("Word limit reached")
            text = "\n".join(textS)
            textwidth, textheight = draw.textsize(text, fontf)
            x = (img.size[0] - textwidth) / 2
            y = (img.size[1] - textheight) / 2
            draw.text((x, y), text, font=fontf, fill=random.choice(colors))
            img.save(vars_setup.newPath(vars_setup.dataBasePath,
                                        vars_setup.newPath(newCatPath, f"Logo-{n}.png")))
            n += 1
        os.startfile(newCatPath)

    """else:
        try:
            userBgSplit = user.split("bgcolor")
            bgSplit2 = userBgSplit[1].split("=")
            bgSplit3 = bgSplit2[1].split(" ")
            bgColor = bgSplit3[0]
            if bgColor == "":
                funcs.printAndSay("Dont add space between '=' and variables")
                raise TypeError("Spaces used between variable and '='")
        except:
            bgColor = "black"

        try:
            userColorSplit = user.split("txt-color")
            bgSplit2 = userColorSplit[1].split("=")
            bgSplit3 = bgSplit2[1].split(" ")
            txtColor = bgSplit3[0]
            if txtColor == "":
                funcs.printAndSay("Dont add space between '=' and variables")
                raise TypeError("Spaces used between variable and '='")
        except:
            txtColor = "white"

        try:
            textS = user.split("=")
            text = textS[-1]
            if text == txtColor:
                funcs.printAndSay("Please enter text")
                raise TypeError("Text Not Given")
            if str(text).startswith("logo"):
                text = text.replace("logo","")
        except:
            text = "No Text Given"

        img = Image.new('RGB', (500, 500), color=bgColor)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(vars_setup.newPath(vars_setup.dataBasePath, "FreeMonoBold.ttf"), 50)
        textS = text.split(" ")
        if len(textS) > 10:
            funcs.printAndSay("Word limit reached [10]")
            raise TypeError("Word limit reached")
        text = "\n".join(textS)
        textwidth, textheight = draw.textsize(text, font)
        x = (500 - textwidth) / 2
        y = (500 - textheight) / 2
        draw.text((x, y), text, font=font, fill=txtColor)
        img.save(vars_setup.newPath(vars_setup.dataBasePath, "latest-logo.png"))
        img.show()"""
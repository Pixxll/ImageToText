from PIL import Image
from os import system, name
import numpy as np
import math


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def img(path, w, h=None, inv=False):
    image = Image.open(path)

    width, height = image.size

    if h is None:
        newWidth = int(w)
        newHeight = round(height / width * newWidth)
    else:
        newWidth = int(w)
        newHeight = int(h)

    newSize = (newWidth, newHeight)

    image = image.resize(newSize).convert('L')

    if inv:
        grayscale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    else:
        grayscale = ".'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    data = np.array(image)

    string = ""
    for i in data:
        line = ""
        for j in i:
            pixel = ""

            charPos = math.floor(int(j) / (255 / len(grayscale)))
            if charPos == 0:
                pixel = pixel + grayscale[0]
            else:
                pixel = pixel + grayscale[(charPos - 1)]

            if line != "":
                line = line + " "

            line = line + pixel
        if string != "":
            string = string + "\n"
        string = string + "| |" + line + "| |"

    edge = ""
    for i in range(newWidth * 2 + 5):
        edge = edge + "-"
    edge += "\n"

    return edge + edge + string + "\n" + edge + edge


#clear()

image = ""
path = ""
while True:
    command = input(">>").split(" ")
    prefix = command[0]

    if prefix.lower() == "stop":
        exit()
    elif prefix.lower() == "clear":
        clear()
    elif prefix.lower() == "load":
        if len(command) == 3:
            image = img(command[1], command[2])
        elif len(command) == 4:
            image = img(command[1], command[2], command[3])

        path = command[1]
    elif prefix.lower() == "show":
        if image != "":
            print(image)
        else:
            print("\u001b[31mNo Image Loaded\u001b[0m")
    elif prefix.lower() == "export":
        if image != "":
            file = open(command[1] + '/' + command[2], 'w')
            file.write(image)
            file.close()
        else:
            print("\u001b[31mNo Image Loaded\u001b[0m")
    elif prefix.lower() == "width":
        if len(command) == 2:
            image = img(path, w)


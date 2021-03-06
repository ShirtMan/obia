import sys
import time
from pathlib import Path
from pyfiglet import Figlet as figlet

class bccolors:
    MAIN = '\033[93m'
    ALT = '\033[94m'
    TITLE = '\033[92m'


def help():
    print('Trash')

def main(args=None):

    if args is None:
        args = sys.argv[1:]

    # setup
    operator = ""


    nameOfItem = ""
    typeOfItem = "Execute"
    commandOfItem = ""

    foundMenu = False

    #----------------------------------------------------------------------

    figText = figlet(font='slant')
    print (bccolors.TITLE + figText.renderText('obia'))

    #get home path
    home = str(Path.home())
    #concant w/ rest of dir
    configDir = home + "/.config/openbox/menu.xml"


    nameOfMenu = input(bccolors.TITLE + '>>>' + bccolors.MAIN + " Name of The Menu: ")
    nameOfItem = input(bccolors.TITLE + '>>>' + bccolors.MAIN + " Name of Menu Item: ")
    commandOfItem = input(bccolors.TITLE + '>>>' + bccolors.MAIN + " Item Command: ")

    idMenu = "id=\"" + nameOfMenu

    #------------------------------------------------------------------------------------


    #TODO find a way to not make this crappy string
    xmlEntry = "        <item label=\"" + nameOfItem + "\">\n            <action name=\"" + typeOfItem + "\">\n                <command>\n                   "+commandOfItem+"\n               </command>\n            </action>\n        </item>\n"

    print(bccolors.ALT + "\nLooking for menu in file...")

    #open file for reading and get contents
    with open(configDir, "r") as sf:
        for line in sf:
            if idMenu in line:
                foundMenu = True
                print("Menu found!")

    with open(configDir, "r") as f:
        content = f.readlines()
        f.close()


    #TODO remove this if statement
    if (foundMenu == False):
        print("Error: Menu " + nameOfMenu + " not found")
        exit()

    #get index
    index = [x for x in range(len(content)) if nameOfMenu in content[x].lower()]

    print("Adding to menu.xml...")

    #insert text into file at index plus 1
    content.insert(index[0] + 1, xmlEntry)

    #write
    f = open(configDir, "w")
    content = "".join(content)
    f.write(content)
    f.close()

    print("Done!")

if __name__ == "__main__":
    main()

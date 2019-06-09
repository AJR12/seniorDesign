import os

def greeting():
    print("\nWelcome to the iMay ANN Trainer!\nLet's start training your new ML model!\n")

    zip = input("\nPlease Drag and Drop your project zip file. Then, Press Enter:\n")
    name = os.path.basename(zip)
    name, ext = name.split(".")
    ext = ext.strip()

    if (' ' in zip) == True:
        i = zip.find(' ')
        print('Space at position:',i)
        print('zip[%s] = ' % i, zip[i])
        print('zip[%i] = ' % (i-1), zip[(i-1)])

    if ("\\" in zip) == True:
        i = zip.find('\\')
        print('\ at position:', i)
        print('zip[%s] = ' % i, zip[i])
        zip = zip.replace('\\','')
        print("New zip =", zip)


greeting()
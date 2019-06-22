import os
from zipfile import ZipFile
from test.labelCounter import labelCounter
import shutil
from stat import S_IXUSR

zipPath = 'C:\Users\deep\Desktop\BallProject.zip'
desPath = '/Users/deep/Desktop'
projName = "testproject"


def unzip(zipPath, desPath, projName):
    labels = []
    with ZipFile(zipPath, 'r') as zipObj:
        # Get a list of all archived file names from the zip
        listOfFileNames = zipObj.namelist()
        # Iterate over the file names
        for fileName in listOfFileNames:
            print("File %s:" % listOfFileNames.index(fileName), fileName)
            count = fileName.count('/')
            # print("/ count:", count)

            #testing label counter
            label = labelCounter(count, fileName)
            if label:
                labels.append(label)
    numLabels = len(labels)

    return numLabels, labels



            # if listOfFileNames.index(fileName) != 0:
            #     # print("^^^")
            #     zipObj.extract(fileName, desPath)

    # rename(desPath, projName)

def rename(desPath, projName):
    projPath = desPath + "/" +projName
    newName = desPath + "/" + projName + "_trainingData"
    os.rename(projPath, newName)

numLabels, labels = unzip(zipPath, desPath, projName)

print('numLabels =', numLabels)
print('labels =', labels)





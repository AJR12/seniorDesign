import os
from zipfile import ZipFile
import shutil

class serverClass:
    def __init__(self):
        self.__zipFilePath = None
        self.__project_name = None
        self.__project_path = None
        self.greeting()
        self.mkdir(self.__project_name)
        self.unzipProj(self.__zipFilePath, self.__project_path, self.__project_name)



    def greeting(self):
        print("\nWelcome to the iMay ANN Trainer!\nLet's start training your new ML model!\n")

        try:
            zip = input("\nPlease Drag and Drop your project zip file. Then, Press Enter:\n")
            name = os.path.basename(zip)
            name, ext = name.split(".")
            ext = ext.strip()

            if ext != "zip":
                raise Exception
        except Exception:
            print('FileTypeError: The file should be a zip file with .zip extension. '
                                'This file has the following extension: .{}'.format(ext))
            print("Please Try Again with the zip created in the iMay GUI")
            self.greeting()
        else:
            # handle whitespace issue is proj has a space
            if ("\\" in zip):
                zip = zip.replace('\\', '')
            if ("\\" in name):
                name = name.replace('\\', '')

            self.__zipFilePath = zip.strip()
            self.__project_name = name



    def mkdir(self, project_name):
        path = os.path.expanduser("~/Desktop/") + project_name

        try:
            os.mkdir(path)
        except OSError as error:
            print("\nCreation of the project %s failed" % path)
            print(error)
            if FileExistsError:
               path = self.fileExistHandled(error, path)
            self.__project_path = path
        else:
            print("Successfully created the project %s " % path)
            self.__project_path = path


    # Handles creating a project that already exists
    def fileExistHandled(self, error, path):
        answer = input("\nProject already exists: Please select one of the options, then Press <Enter>:\n"
                       "<R> Replace this Project\t<K> Keep Both Projects\t<C> Cancel New Project\n")
        answer = answer.upper()
        # Check if the user entered correctly
        if answer != "R" and answer != "K" and answer != "C":
            x = True
            while x:
                answer = input(
                    "\n**Incorrect Entry: Please select <R>, <K>, or <C>**"
                    "\nProject already exists: Please select one of the options, then Press <Enter>:\n"
                    "<R> Replace this Project\t<K> Keep Both Projects\t<C> Cancel New Project\n")
                answer = answer.upper()
                if answer == "R" or answer == "K" or answer == "C":
                    x = False
        # handle <R>
        if answer == "R":
            shutil.rmtree(path)
            os.mkdir(path)
        # handle <K>
        elif answer == "K":
            x = True
            while x:
                try:
                    path = path + " (1)"
                    os.mkdir(path)
                except OSError as error:
                    if FileExistsError:
                        pass
                    else:
                        print(error)
                else:
                    print("New project created: %s" % path)
                    x =False
        # handle <C>
        elif answer == "C":
            print("\nOk, cancelling project. Thank you!")
            input()
            exit()
        return path

    # Extract project zip file
    def unzipProj(self, zipFilePath, desPath, projName):
        with ZipFile(zipFilePath, 'r') as zipObj:
            listOfFileNames = zipObj.namelist()
            for fileName in listOfFileNames:
                print("File %s:" % listOfFileNames.index(fileName), fileName)

                if not fileName.startswith("__") and not fileName.endswith(projName + "/") \
                        and listOfFileNames.index(fileName) != 0 and listOfFileNames.index(fileName) != 1:
                    print('^^^')
                    zipObj.extract(fileName, desPath)
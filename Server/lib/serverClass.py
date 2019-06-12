import os
from zipfile import ZipFile
import shutil

class serverClass:
    def __init__(self):
        self.__zipFile_path = None
        self.__project_name = None
        self.__project_path = None
        self.__trainData_path = None
        self.labels = []
        self.greeting()
        self.mkdir(self.__project_name)
        self.unzipProj(self.__zipFilePath, self.__project_path, self.__project_name)
        self.numLabels = len(self.labels)


    # Greets the user
    def greeting(self):
        """
        Here we greet the user. You drag and drop the .zip created in the GUI.
        :return: self.__zipFilePath
                 self.__project_name
        """
        print("\nWelcome to the iMay ANN Trainer!\nLet's start training your new ML model!\n")
        # make sure that the file entered is a .zip file
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
            # if ("\\" in zip):
            #     zip = zip.replace('\\', '')
            # if ("\\" in name):
            #     name = name.replace('\\', '')

            self.__zipFilePath = zip.strip()
            self.__project_name = name

    # Creates new dir for the proj entered
    def mkdir(self, project_name):
        """
        Here we make a new project directory to extract the .zip files in. Name of new dir is the project name
        the user selected.
        :param project_name:
        :return: self.__project_path
        """
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
        """
        Method used inside of mkdir() method. Handles issue of dir with project name already exists
        :param error:
        :param path:
        :return:
        """
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
        """
        Here we unzip the project .zip file in the new proj dir. the extracted folder contains
        subdirs with label names.
        :param zipFilePath: path to .zip file
        :param desPath: path to proj dir
        :param projName:
        :return: self.labels.
        """
        with ZipFile(zipFilePath, 'r') as zipObj:
            listOfFileNames = zipObj.namelist()
            for fileName in listOfFileNames:
                # print("File %s:" % listOfFileNames.index(fileName), fileName)
                self.labelCounter(fileName)
                if not fileName.startswith('__'):
                    # print('^^^')
                    zipObj.extract(fileName, desPath)
        self.renameTrainingDataDir(desPath, projName)

    # Counts number of labels
    def labelCounter(self, fileName):
        """
        Counts number of labels. Used in unzipProj() method
        :param fileName:
        :return: self.labels.
        """
        count = fileName.count('/')
        if count == 2 and fileName.endswith('/'):
            a, b, c = fileName.split('/')
            self.labels.append(b)

    # Renames extracted .zip dir
    def renameTrainingDataDir(self, desPath, projName):
        """
        Renames extracted .zip dir. Used in unzipProj() method
        :param desPath:
        :param projName:
        :return: self.__trainData_path
        """
        projPath = desPath + "/" + projName
        newName = desPath + "/" + projName + "_trainingData"
        os.rename(projPath, newName)
        self.__trainData_path = newName

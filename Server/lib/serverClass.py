import os

class serverClass:
    def __init__(self):
        self.project_name = None
        self.greeting()
        self.mkdir(self.project_name)


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
            self.project_name = name

    def mkdir(self, project_name):
        path = os.path.expanduser("~/Desktop/") + project_name

        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)



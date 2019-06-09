import os
from zipfile import ZipFile
import shutil
from stat import S_IXUSR

zipPath = '/Users/antonio/Downloads/test project.zip'
desPath = '/Users/antonio/Desktop'
proj_name = "test project"



with ZipFile(zipPath, 'r') as zipObj:
   # Get a list of all archived file names from the zip
   listOfFileNames = zipObj.namelist()
   # Iterate over the file names
   for fileName in listOfFileNames:
       print("File %s:" % listOfFileNames.index(fileName), fileName)

       if not fileName.startswith("__") and listOfFileNames.index(fileName) != 0 and listOfFileNames.index(fileName) != 1:
           print("^^^")
           zipObj.extract(fileName, desPath)




       # Check filename endswith csv
       # if fileName.endswith('.csv'):
       #     # Extract a single file from zip
       #     zipObj.extract(fileName, 'temp_csv')



# ZIP_UNIX_SYSTEM = 3
#
# def extract_all_with_executable_permission(zf, target_dir):
#   for info in zf.infolist():
#     extracted_path = zf.extract(info, target_dir)
#
#     if info.create_system == ZIP_UNIX_SYSTEM and os.path.isfile(extracted_path):
#       unix_attributes = info.external_attr >> 16
#       if unix_attributes & S_IXUSR:
#         os.chmod(extracted_path, os.stat(extracted_path).st_mode | S_IXUSR)
#
# with zipfile.ZipFile(zipPath, 'r') as zf:
#   extract_all_with_executable_permission(zf, desPath)


# unZipFile = zipfile.ZipFile(zipPath, "r")
#
# tmp_dir = desPath
# try:
#     for info in unZipFile.infolist():
#         real_path = unZipFile.extract(info, tmp_dir)
#
#         # permission
#         unix_attributes = info.external_attr >> 16
#         target = os.path.join(tmp_dir, info.filename)
#         if unix_attributes:
#             os.chmod(target, unix_attributes)
#
#         if not real_path:
#             print ("Extract failed: " + info.filename)
# finally:
#     unZipFile.close()


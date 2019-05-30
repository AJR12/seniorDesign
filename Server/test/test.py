import os

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
print(desktop)








dirName = 'tempDir'

try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
except FileExistsError:
    print("Directory ", dirName, " already exists")
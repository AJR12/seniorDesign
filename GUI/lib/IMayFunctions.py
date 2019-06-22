import shutil
import os


def create_directory(dirName):
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


def copy_directory(paths, labels,dest):
    print("test")
    for i in range(len(paths)):
        shutil.copytree(paths[i], dest + '/' + labels[i])


def zip_files(output_file, dir_path):
    outputs = output_file
    inputs = dir_path
    shutil.make_archive(inputs, 'zip', outputs)
    #for i in range(len(inputs)):
        #shutil.make_archive(inputs[i], 'zip', outputs[i])


def rename(dir_path, name):
    path = dir_path
    files = os.listdir(path)
    i = 0

    for file in files:
        os.rename(os.path.join(path, file), os.path.join(path, name + str(i) + '.jpg'))
        i = i + 1


#create_directory("Imay_test")
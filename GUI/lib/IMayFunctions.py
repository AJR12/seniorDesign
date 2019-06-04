import shutil
import os


def zip_files(output_file, dir_path):
    outputs = output_file
    inputs = dir_path
    for i in range(len(inputs)):
        shutil.make_archive(outputs[i], 'zip', inputs[i])


def rename(dir_path, name):
    path = dir_path
    files = os.listdir(path)
    i = 0

    for file in files:
        os.rename(os.path.join(path, file), os.path.join(path, name + str(i) + '.jpg'))
        i = i + 1


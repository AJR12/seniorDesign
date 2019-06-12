import os


__trainingData_path = '/Users/deep/Desktop/testproject/testproject_trainingData'

# while os.walk(__trainingData_path):

# _, labels, files = os.walk(__trainingData_path)
# print("_ =", _)
# print("labels:", labels)
# print("Files:", files)


def labelFileCounter(__trainingData_path):
    numFiles = numLabels = 0
    for _, labels, files in os.walk(__trainingData_path):
      # ^ this idiom means "we won't be using this value"
        print("_ =", _)
        print("labels:", labels)
        print("Files:", files)
        numFiles += len(files)
        numLabels += len(labels)

    print ("{:,} files, {:,} folders".format(numFiles, numLabels))

labelFileCounter(__trainingData_path)
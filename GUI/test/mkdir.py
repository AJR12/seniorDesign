import os



# path = input("Where do you want to unzip the file? %s" %os.path.expanduser("~") )
# path = os.path.expanduser("~") + path
# print("\n", path)

#   /Users/antonio/Downloads/blood-cells.zip

zip = input("\nDrag and Drop zip file:\n")
name = os.path.basename(zip)
name, ext = name.split(".")

# print("Type(test):", type(test), "test:", test)
# print("Type(ext):", type(ext), "ext:", ext)

# print("name =", name)
#
# print("ext =", ext)
# print("len(ext) =", len(ext))
# print(type("zip"))





def mkdir(projectName):

    path = os.path.expanduser("~/Desktop/") + projectName

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

if ext != "zip":
    print("bad")
else:
    print("good")
    mkdir(name)
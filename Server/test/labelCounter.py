def labelCounter(count, fileName):
    label = None
    if count == 2 and fileName.endswith('/'):
        print("^^^ This is a Label")
        a, b, c = fileName.split('/')
        # print("split test: a = {} \t b = {} \t c = {}".format(a, b, c))
        # print('len(c) =', len(c))
        label = b
        return label


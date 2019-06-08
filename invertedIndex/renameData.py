import os


# Function to rename multiple files
def rename():
    i = 0
    path = os.path.join(os.path.dirname(__file__), "../data")
    if not os.path.isdir(path):
        raise OSError("can not find directory {0}".format(path))
    files = os.listdir(path)
    files.sort(key=lambda x: int(x.split(".")[0]))
    for filename in files:
        src = os.path.join(path, filename)
        dst = os.path.join(path, str(i) + ".html")
        os.rename(src, dst)
        i += 1

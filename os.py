import os

def safe_mv(file, newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    os.rename(file, newpath)
import os

path = "D:"#文件路径

originalname = '' #指定字符
replacename = ''  #替换字符


def rename_file(filepath):
    files = os.listdir(filepath)
    for file in files:
        if os.path.isdir(filepath + '\\' + file):
            rename_file(filepath + '\\' + file)
        else:
            subFiles = os.listdir(filepath + '\\')
            for subFile in subFiles:
                if originalname in subFile:
                    n = str(filepath + '\\' + subFile.replace(originalname, replacename))
                    n1 = str(filepath + '\\' + str(subFile))
                    try:
                        os.rename(n1, n)
                    except IOError:
                        continue


rename_file(path)

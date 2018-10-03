import os
from fnmatch import fnmatch
import string
def fpath(root):
    pattern = "*.jpg"
    l=[]
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern) or fnmatch(name,'*.png')  :
                l.append(os.path.join(path,name))
                #print (l)
        l1=[]
        for i in range(len(l)):
            new_str=l[i].replace('\\','\\\\')
            l1.append(new_str)
        return (l1)


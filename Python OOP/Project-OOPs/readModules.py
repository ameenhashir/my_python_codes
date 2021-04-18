import myfunctions
#import module1.myfunctions_1 as mf
from module1 import myfunctions_1 as mf
# import is used to import a python file
# from is used to specify location of directory of python file

r1 = myfunctions.add(2,4)
print(r1)

r1 = mf.add(2,4)
print(r1)
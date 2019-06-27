from ctypes import *
import time
rd = cdll.LoadLibrary('../build/libreader.so')

rd.readdata.restype=c_char_p
for i in range(1,100):
  #  wt.spdreader.restype=(c_int)
# wt.spdreader.argtypes=()
    str = rd.readdata()
    print(str)
#for i in range(1,100):
#   f2 = rd.myreader()

    




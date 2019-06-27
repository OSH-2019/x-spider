from ctypes import *
import time
wt = cdll.LoadLibrary('../build/libwriter.so')
#rd = cdll.LoadLibrary('../build/libreader.so')



for i in range(1,100):
    wt.spdwriter.restype=(c_long)
    wt.spdwriter.argtypes=(c_char_p,c_int,c_short,c_byte)
    str1 = c_char_p(bytes("ss",'utf-8'))
    f1 = wt.spdwriter(str1,10,1,0)
    print(f1)

#for i in range(1,100):
#   f2 = rd.myreader()

    




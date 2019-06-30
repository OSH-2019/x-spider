from ctypes import *
import time
wt = cdll.LoadLibrary('../build/libwriter.so')
rd = cdll.LoadLibrary('../build/libreader.so')


wt.spdwriter.restype=(c_long)
wt.spdwriter.argtypes=(c_char_p,c_int,c_short,c_byte)
rd.spdreaddata.restype=(c_char_p)
rd.spdreaddata.argtypes=(c_long,c_int)
for i in range(1,10):
    str2 = 'rer'+str(i)+'dfd' 
    str1 = c_char_p(bytes(str2,'utf-8'))
    f1 = wt.spdwriter(str1,10,1,0)
    #print('python:{0}'.format(f1))
    f2 = rd.spdreaddata(f1,1)
    print(str1)
    print(f2)



    #for i in range(1,100):
#   f2 = rd.myreader()

    




from ctypes import *

read = CDLL('/home/wowo/work/osh/yjj/yijinjing-lite/build/libreader.so')
#read.reader.argtypes = ()
write = CDLL('/home/wowo/work/osh/yjj/yijinjing-lite/build/libwriter.so')
#write.writer.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def our_function(numbers):
    global write
    num_numbers = len(numbers)
    array_type = c_int * num_numbers
    write.writer(c_int(num_numbers), array_type(*numbers))


our_function([1,2,3,4,5,6])
read.reader.restype = POINTER(c_int)
result = read.reader()
print(result[0:6])

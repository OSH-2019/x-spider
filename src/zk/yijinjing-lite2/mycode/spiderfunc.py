from ctypes import *

wt = cdll.LoadLibrary('../build/libwriter.so')
rd = cdll.LoadLibrary('../build/libreader.so')

wt.spdwriter.restype=(c_long)
wt.spdwriter.argtypes=(c_char_p,c_int,c_short,c_byte)
rd.spdReadSingleData.restype=(c_char_p)
rd.spdReadSingleData.argtypes=(c_long,c_int)
rd.spdReadSingleMsgType.restype=(c_int)
rd.spdReadSingleMsgType.argtypes=(c_long,c_int)
rd.spdPrintAllData.argtypes=(c_long,c_int)
rd.spdConvertAllToCSV.restype=(c_int)
rd.spdConvertAllToCSV.argtypes=(c_long,c_char_p)

#return time stamp
def writeSingleData(data,msgType):
    strwt = c_char_p(bytes(data,'utf-8'))
    lenwt = len(data)
    #print('this is lenth:{name}'.format(name=lenwt))
    wtime = wt.spdwriter(strwt,lenwt,msgType,0)
    return wtime

#return single data as bytes 
def readSingleData(readtime):
    strrd = rd.spdReadSingleData(readtime,0)
    return strrd

#return single MsgType
def readSingleMsgType(readtime):
    msgType = rd.spdReadSingleMsgType(readtime,0)
    return msgType

#def getNextFrame(time):

#print all data from startTime    
def printAllData(startTime):
    rd.spdPrintAllData(startTime,0)
   
#convert all data from startTime to .csv file named by fileName
def convertAllToCSV(startTime,fileName):
    fileName = c_char_p(bytes(fileName,'utf-8'))
    res = rd.spdConvertAllToCSV(startTime,fileName)


    


'''
if __name__ == '__main__':
    for i in range(1,10):
        str2 = 'rer'+str(i)+'dfd' 
        str1 = c_char_p(bytes(str2,'utf-8'))
        f1 = wt.spdwriter(str1,10,1,0)
        #print('python:{0}'.format(f1))
        f2 = rd.spdReadSingleData(f1,1)
        print(str1)
        print(f2)
'''


    #for i in range(1,100):
#   f2 = rd.myreader()

    




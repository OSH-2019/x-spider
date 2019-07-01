from ctypes import *

wt = cdll.LoadLibrary('../build/libwriter.so')
rd = cdll.LoadLibrary('../build/libreader.so')

wt.spdwriter.restype=(c_long)
wt.spdwriter.argtypes=(c_char_p,c_int,c_short,c_byte,c_char_p)
wt.spdReadCSV.restype=(c_int)
wt.spdReadCSV.argtypes=(c_char_p,c_char_p)

rd.spdReadSingleData.restype=(c_char_p)
rd.spdReadSingleData.argtypes=(c_long,c_char_p)
rd.spdReadSingleMsgType.restype=(c_int)
rd.spdReadSingleMsgType.argtypes=(c_long,c_char_p)
rd.spdPrintAllData.argtypes=(c_long,c_char_p)
rd.spdConvertAllToCSV.restype=(c_int)
rd.spdConvertAllToCSV.argtypes=(c_long,c_char_p,c_char_p)
rd.spdExpireJournal.restype=(c_bool)
rd.spdExpireJournal.argtype=(c_char_p)
rd.spdExpireJournalByIndex.restype=(c_bool)
rd.spdExpireJournalByIndex.argtype=(c_int,c_char_p)

#return time stamp
def writeSingleData(data,msgType,jname):
    strwt = c_char_p(bytes(data,'utf-8'))
    lenwt = len(data)
    jname = c_char_p(bytes(jname,'utf-8'))
    #print('this is lenth:{name}'.format(name=lenwt))
    wtime = wt.spdwriter(strwt,lenwt,msgType,0,jname)
    return wtime

#return single data as bytes 
def readSingleData(readtime,jname):
    jname = c_char_p(bytes(jname,'utf-8'))
    strrd = rd.spdReadSingleData(readtime,jname)
    return strrd

#return single MsgType
def readSingleMsgType(readtime,jname):
    jname = c_char_p(bytes(jname,'utf-8'))
    msgType = rd.spdReadSingleMsgType(readtime,jname)
    return msgType

#def getNextFrame(time):

#print all data from startTime    
def printAllData(startTime,jname):
    jname = c_char_p(bytes(jname,'utf-8'))
    rd.spdPrintAllData(startTime,jname)
   
#convert all data from startTime to .csv file named by fileName
def convertAllToCSV(startTime,fileName,jname):
    jname = c_char_p(bytes(jname,'utf-8'))
    fileName = c_char_p(bytes(fileName,'utf-8'))
    res = rd.spdConvertAllToCSV(startTime,fileName,jname)

#useless function
def expireJournal(journalName):
    journalName = c_char_p(bytes(journalName,'utf-8'))
    flag = rd.spdExpireJournal(journalName)

#useless function 
def initJournal(dir,jname):
    dir = c_char_p(bytes(dir,'utf-8'))
    jname = c_char_p(bytes(jname,'utf-8'))
    wt.spdInitJournal(dir,jname)

#useless function
def expireJournalByIndex(index,journalName):
    journalName = c_char_p(bytes(journalName,'utf-8'))
    flag = rd.spdExpireJournalByIndex(index)

#read .csv to yjj
def readCSV(filename,jname):
    filename = c_char_p(bytes(filename,'utf-8'))
    jname = c_char_p(bytes(jname,'utf-8'))
    flag = wt.spdReadCSV(filename,jname)
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

    




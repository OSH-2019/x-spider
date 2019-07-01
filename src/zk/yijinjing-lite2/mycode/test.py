import spiderfunc

'''
wtime = spiderfunc.writeSingleData('start',2,'test3')
for i in range(1,10):
    wtime1 = spiderfunc.writeSingleData('dd'+str(i),1,'test3')
'''

spiderfunc.readCSV('data1.csv','ts')
#spiderfunc.convertAllToCSV(0,'data1.csv','test1')
spiderfunc.printAllData(0,'ts')

import spiderfunc

'''
wtime = spiderfunc.writeSingleData('start',2,'test3')
for i in range(1,10):
    wtime1 = spiderfunc.writeSingleData('dd'+str(i),1,'test3')
'''

spiderfunc.expireJournal('test3')

spiderfunc.printAllData(0,'test3')

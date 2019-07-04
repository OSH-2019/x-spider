import spiderfunc

n = 4000
wtime = [0]*n
interval = [0]*n
mean = 0
square = 0
max = 0
min = 0

for i in range(0,n):
    wtime[i] = spiderfunc.writeSingleData('ss',1,'test4')
    
for i in range(1,n):    
    interval[i-1] = wtime[i]-wtime[i-1]

mean = (wtime[n-1]-wtime[0])/(n-1)
min = interval[0]
for i in range(0,n-1):
    square = (interval[i]-mean)*(interval[i]-mean)+square
    if(interval[i]<min):
        min = interval[i]
    if(interval[i]>max):
        max = interval[i]

if(interval[n-1]<min):
    min = interval[n-1]
if(interval[n-1]>max):
    max = interval[n-1]

square = square/(n-1)
std = square ** 0.5

print('mean:{0}'.format(mean))
print('std:{0}'.format(std))
print('min:{0}'.format(min))
print('max:{0}'.format(max))

for i in range(0,10):
    print(interval[i])



#spiderfunc.convertAllToCSV(0,'data1.csv','test1')
#spiderfunc.printAllData(0,'data.csv')

#__author__ = 'spider'
from rain.client import Client,remote,Output
import requests
# requests 用于爬取新浪股票 API
import time
import sys
# sys 用于在解释器中交互
import threading
# threading 用于多线程处理    

from queue import Queue
# Queue 是有关队列的库
from optparse import OptionParser
# OptionParser 用于在命令行中添加选项
client = Client("localhost",7210)

from ctypes import *

def printAllData(startTime,jname,rd):
    jname = c_char_p(bytes(jname,'utf-8'))
    rd.spdPrintAllData(startTime,jname)

def writeSingleData(data,msgType,jname,wt):
    strwt = c_char_p(bytes(data,'utf-8'))
    lenwt = len(data)
    jname = c_char_p(bytes(jname,'utf-8'))
    #print('this is lenth:{name}'.format(name=lenwt))
    wtime = wt.spdwriter(strwt,lenwt,msgType,0,jname)
    return wtime

def strategy(vector):
    result="{} WAIT".format(vector[1][0])
    suma=0  #20
    sumb=0  #5
    for i in range(1,21):
        suma = suma + float(vector[i][1])
    
    for i in range(16,21):
        sumb = sumb + float(vector[i][1])
    
    meana = suma / 20
    meanb = sumb / 5

    ans = 0
    if(meana < meanb):
        ans = 1 + round((meanb-meana)/0.01)
        result = "{}  BUY: {}".format(vector[1][0],ans)
        vector[0] += ans
    elif meana > meanb and vector[0] != 0 :
        ans = vector[0]
        result = "{}  SOLD: {}".format(vector[1][0],ans)
        vector[0] = 0
    return result


class Analysis():
    def __init__(self,analysis_queue):
        #threading.Thread.__init__(self)
        self.analysis_queue = analysis_queue
        #self.start()
        self.vector={}
        
    def run(self,files,wt,rd):
        result = self.analysis_queue.get()
        print("**********start**********")
        for obj in result: 
            writeSingleData(",".join(obj),1,obj[0],wt)
            self.vector.setdefault(obj[0],[0])  
            self.vector[obj[0]].append((obj[0],obj[3]))
            result=()
            if len(self.vector[obj[0]]) == 20 + 1 + 1:
                del self.vector[obj[0]][1]
                result = strategy(self.vector[obj[0]])
                files.write(obj[30] + "," + obj[31] + "," + result +"\n")
        print("**********end**********")
                

class Worker(threading.Thread):
# 创建类 Work，多线程获取

    def __init__(self, work_queue, result_queue,analysis_queue):
    # 写入必须绑定的强制属性 self， work_queue， result_queue
    # __init__ 方法的第一个参数一定是 self，用于表示创建的实例本身
    # 其中，实例是根据类来创建的
    # 在 __init__ 方法内部，可将各种属性绑定到 self，因为 self 指向创建的实例本身

        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.result_queue = result_queue
        self.analysis_queue = analysis_queue
        self.start()

    def run(self):
    # 增加一个新方法 run

        while True:
            func, arg, code_index = self.work_queue.get()
            # 获取 func, arg, code_index
            res = func(arg, code_index)
            #res = tuple(res)
            self.result_queue.put(res)
            if self.result_queue.full():
                #res=self.result_queue.get() for i in range(self.result_queue.qsize())
                result = sorted([self.result_queue.get() for i in range(self.result_queue.qsize())], key=lambda s: s[0], reverse=True)
                # sorted() 是用于排序的方法，返回副本，原始输入不变
                # Queue.get() 用于获取队列
                # Queue.qsize() 返回队列大小         
                # key=lambda s: s[0]：关键词为 lambda s: s[0]
                # lambda s: s[0]：匿名函数，返回第一个元素
                # reverse=True：降序排列      
                #res.insert(0, ('0', u'名称     股价'))
                # list.insert() 用于将指定对象插入列表的指定位置   
                '''
                print ('***** start *****')
                for obj in res:
                    print(type(obj))
                    for i in obj:
                        print(i,end=" ")
                
                        
                    #print(obj[1])
                print ('***** end *****\n')
                '''
                self.analysis_queue.put(result)
            self.work_queue.task_done()
            # 在完成一项工作后，Queue.task_done() 会向任务已经完成的队列发送一个信号       


class Stock(object):
# 股票实时价格获取

    def __init__(self, code, thread_num,queue):
        self.code = code
        self.work_queue = Queue()
        self.analysis_queue = queue
        self.threads = []
        self.__init_thread_poll(thread_num)

    def __init_thread_poll(self, thread_num):
        self.params = self.code.split(',')
        # parmas 会向函数传入一个字典
        #self.params.extend(['s_sh000001', 's_sz399001'])  
        # 默认获取沪指、深指
        # extend()： 扩展，与 append() 的区别为，extend() 加入的元素是分别单个加入的
        self.result_queue = Queue(maxsize=len(self.params[::-1]))
        
        for i in range(thread_num ):
            self.threads.append(Worker(self.work_queue, self.result_queue,self.analysis_queue))
        #self.threads.append(Analysis(self.analysis_queue))
    def __add_work(self, stock_code, code_index):
        self.work_queue.put((self.value_get, stock_code, code_index))
        # self.value_get 涉及到下面的装饰器        

    def del_params(self):
        for obj in self.params:
            self.__add_work(obj, self.params.index(obj))

    def wait_all_complete(self):
        for thread in self.threads:
            if thread.isAlive():
            # 判断线程是否是激活的
            # 从调用 start() 方法启动线程，到 run() 方法执行完毕或者遇到未处理异常而中断，这段时间内线程是激活的           
                thread.join()
                # join() 的作用是阻塞进程直到线程执行完毕
                # 依次检查线程池中的线程是否接触，没有结束就阻塞线程直到线程结束
                # 如果结束则跳转执行下一个线程的 join() 函数                 

    @classmethod
    # 装饰器，返回函数的高阶函数    
    def value_get(cls, code, code_index):
        '''
        slice_num, value_num = 21, 3
        name, now = u'——无——', u'  ——无——'
        if code in ['s_sh000001', 's_sz399001']:
            slice_num = 23
            value_num = 1
        '''
        r = requests.get("http://hq.sinajs.cn/list=%s" % (code,))
        # 爬取新浪股票 API                
        res = r.text.split(',')
        '''
        if len(res) > 1:
            name, now = r.text.split(',')[0][slice_num:], r.text.split(',')[value_num]
        '''
        res[0]=res[0][21:]
        return res
        

@remote(outputs=0)
def Task(ctx, nlist, thread_num, sleep_time):
    files=open("/root/ans.txt","w")
    files.write("a,saad\n")
    sys.path.append("/root")
    #__import__("spiderfunc")
    wt = cdll.LoadLibrary('/root/libwriter.so')
    rd = cdll.LoadLibrary('/root/libreader.so')
    #files.write("fsdjkfsjkfhkj")
    liststr = ",".join(nlist)
    analysis_queue = Queue()
    stock = Stock(liststr, thread_num, analysis_queue)
    analysis = Analysis(analysis_queue)
    for k in range(50):
        stock.del_params()
        analysis.run(files,wt,rd)
        time.sleep(0.01)
    files.close()

if __name__ == '__main__':
# 该脚本用于直接运行，而不能被 import
    parser = OptionParser(description="Query the stock's value.", usage="%prog [-c] [-s] [-t]", version="%prog 1.0")
    # 生成命令行说明
    # %prog 将会以当前程序名的字符串来代替    
    parser.add_option('-c', '--stock-code', dest='codes',
                      help="the stock's code that you want to query.")
    # 使用 add_option() 来定义命令行参数，即加入选项
    # dest 是储存的变量                     
    parser.add_option('-s', '--sleep-time', dest='sleep_time', default=1, type="int",
                      help='How long does it take to check one more time.')
    parser.add_option('-t', '--thread-num', dest='thread_num', default=3, type='int',
                      help="thread num.")
    options, args = parser.parse_args(args=sys.argv[1:])
    # 设置好命令行后，用 parse_args() 来解析命令行
    assert options.codes, "Please enter the stock code!"  
    # 是否输入股票代码
    
    
    codeslist = options.codes.split(',')
    if list(filter(lambda s: s[:-6] not in ('sh', 'sz', 's_sh', 's_sz'), codeslist)):  
    # 股票代码输入是否正确
        raise ValueError

    with client.new_session("localhost",) as session:
        listlist = []
        for i in range(0, len(codeslist), 5):
            if(i + 5 <= len(codeslist)):
                listlist.append(codeslist[i: i+5])
            else :
                listlist.append(codeslist[i:])
        for codes in listlist:
            task=Task(codes, options.thread_num, options.sleep_time)
        
        session.submit()
        session.wait_all()
        




import getopt
import sys, random, os
from . import tools
from time import sleep, time
from multiprocessing import Process, Lock

class ModeError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self,ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return  self.errorinfo

def main(argv):

    try:
        opts, args = getopt.getopt(argv, 'n:f:w:h', ['ip=', 'num=', 'function=','help'])
        # print('指令参数:',opts,'   额外参数:',args)
    except getopt.GetoptError:
        print('Error: python scanner.py -n <thread_num> -f <function:tcp/ping> --ip <ip/ip range> -w <filename.txt>')
        sys.exit(2)

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ('-n', '--num'):
            thread_num = int(arg)
        elif opt in ('-f', '--function'):
            mode = arg
        elif opt in ('--ip'):
            ip = arg
        elif opt in ('-w'):
            file = arg
        elif opt in ('-h','--help'):
            print('Please type like following::')
            print('python scanner.py -n <thread_num> -f <function:tcp/ping> --ip <ip/ip range> -w <filename.txt>')
            sys.exit()

    print('模式:',mode)
    print('线程数:',thread_num)
    print('ip/ip段:',ip)
    print('结果存储名称:',file)

    if mode == "tcp":
        tools.ScanPort(ip,thread_num,file)
    elif mode == "ping":
        tools.ScanPing(ip,thread_num,file)
    else:
        raise ModeError(f'请在-f后输入tcp/ping,你输入的是{mode}')

def run(l,i):
    print("%s子进程开始，进程ID：%d" % (i,os.getpid()))
    l.acquire()
    start = time()
    sleep(random.choice([1, 2, 3, 4]))
    main(sys.argv[1:])
    end = time()
    l.release()
    print("%s子进程结束，进程ID：%d。耗时0.2%f" % (i,os.getpid(), end-start))
if __name__ == "__main__":
    lock = Lock()
    for num in range(2):
        Process(target=run, args=(lock, num)).start()
        
        
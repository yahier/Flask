# -*- coding: UTF-8 -*-

import thread
import time
import threading

# 线程的结束一般依靠线程函数的自然结束；也可以在线程函数中调用thread.exit()，他抛出SystemExit exception，达到退出线程的目的。
# 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。


# 为线程定义一个函数
def print_time1( threadName, delay):
   #print('print')
   count = 0
   while count < 5:
      print('while')
      time.sleep(delay)
      count += 1
      print "%s: %s" % (threadName, time.ctime(time.time()))



# 创建两个线程
def startThread1():
   try:
      thread.start_new_thread(print_time1, ("Thread-1", 2))
      thread.start_new_thread(print_time1, ("Thread-2", 4))
      print('try')
   except:
      print "Error: unable to start thread"
   while 1:
         pass




#用threading模块创建线程
exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        print_time2(self.name, self.counter, 5)
        print "Exiting " + self.name

def print_time2(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

def startThread2():
   thread1 = myThread(3, "Thread-3", 1)
   thread2 = myThread(4, "Thread-4", 2)
   # 开启线程
   thread1.start()
   thread2.start()

if __name__ == '__main__':
   #startThread1()
   startThread2()

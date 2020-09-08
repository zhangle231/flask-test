# docker添加外部存储

docker volume rm qamg
docker volume rm qacode

docker volume create --name=qamg
docker volume create --name=qacode

# 创建测试账号

docker exec -it quantaxis_docker_qatrader_1 /bin/bash

qatrader --acc 'x1'--pwd 'x1' --broker QUANTAXIS

# 查询账号信息

查询账户组合: http://101.200.36.215:8020/tradeaccounts?action=list_sim


# 接口方式，获取用户

from QIFIAccount import QIFI_Account, ORDER_DIRECTION
acc = QIFI_Account("x1", "x1")
acc.initial()


# 获取行情

import QUANTAXIS as QA

QA.QA_fetch_stock_day_adv('000001','2020-08-25', '2020-08-26')
QA.QA_fetch_stock_day_adv('rb1910','2020-08-25', '2020-08-26')


# 发送定单

from QAPUBSUB import producer
import json
import datetime

p = producer.publisher_routing(
    user='admin', password='admin', host='127.0.0.1', exchange='QAORDER_ROUTER')

p.pub(json.dumps({
    'topic': 'sendorder',
    'account_cookie': 'x1',
    'strategy_id': 'test',
    'code': 'rb1910',
    'price': 1500,
    'order_direction': 'BUY',
    'order_offset': 'OPEN',
    'volume': 1,
    'order_time': str(datetime.datetime.now()),
    'exchange_id': 'SHFE'
}), routing_key='x1')




p.pub(json.dumps({
    'topic': 'sendorder',
    'account_cookie': 'x1',
    'strategy_id': 'test',
    'code': '000001',
    'price': 1500,
    'order_direction': 'BUY',
    'order_offset': 'OPEN',
    'volume': 1,
    'order_time': str(datetime.datetime.now())
}), routing_key='x1')



# 我的接口

## 文档
http://101.200.36.215:9000/doc

## 接口
http://101.200.36.215:9001/


## 查询银行 [POST] (实盘独有API)

http://101.200.36.215:8020/order?action=query_bank&acc=1010101&type=real&bank_id=1

http://101.200.36.215:8020/tradeaccounts?action=query_accounthistory&account_cookie=1010101

http://101.200.36.215:8020/tradeaccounts?action=query_account&account_cookie=1010101

## 实时获取信息
def __getattr__(self, item):                                   
    try:                                                       
        api = self.get_available()                             
        func = api.__getattribute__(item)                      
                                                               
        def wrapper(*args, **kwargs):                          
            res = self.executor.submit(func, *args, **kwargs)  
            self._queue.put(api)                               
            return res                                         
        return wrapper                                         
    except:                                                    
        return self.__getattr__(item) 


## 学习一下QAEngine
QA_Event
QA_Worker
QA_Task
QA_Thread
QA_Engine
QA_AsyncThread
QA_AsyncQueue
QA_AsyncExec
QA_AsyncTask
QA_AsyncScheduler
create_QAAsyncScheduler

### QA_Event

下面是一个高级玩法，通过exec动态的增加了python语句

# This statement supports dynamic execution of Python code
for item in kwargs.keys():
    exec('self.{}=kwargs[item]'.format(item))

QA_Event主要是一个可执行的实体，记录了func和callback

### QA_Worker

从abc中提供了抽象方法

from abc import abstractmethod

👻QA_Broker 继承这个类
👻QA_Account 继承这个类
👻QA_OrderHandler 继承这个类

这个类啥也没干，主要是run方法，需要子类继承

### QA_Task

QA_Task就是把event和work合在一起，主要就是do方法，负责执行work的run方法，并执行callback.

    def do(self):
        self.res = self.worker.run(self.event)
        if self.callback:
            self.callback(self.res)

此外学到@property，这个可以定义类的只读属性

### QA_Thread

在"QUANTAXIS/QAEngine/QAThreadEngine.py"模块中，继承自threading.Thread。QA_Engine 继承这个类。

QA_Thread继承threading.Thread。run方法中执行实际的任务，通过Queue来获取任务

QA_Engine继承自QA_Thread，增加了kernels

学习使用：threading.Event 

Event主要方法
set()
clear()
wait()

知道上面这几个就够了，首先set相当于true,clear相当于false,然后wait如果是clear的化会一直等待

### QA_AsyncThread

也是继承于threading.Thread

self.ident这个是线程的id

学习以下语法结构，代表有异常跳过，没有异常，执行else中的块
```
try:
     event = self.queue.get_nowait()
 except asyncio.QueueEmpty:
     pass
 else:
     asyncio.run_coroutine_threadsafe(
```



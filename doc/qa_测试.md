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

下面是一个最小的asyncio的使用场景，asyncio主要就是通过单一进程来模拟多线程，解决阻塞问题，解决的方法则是通过消息循环来完成的。
new_event_loop()创建一个新的循环，就像多线程中申请了一个新的线程一样；
run_until_complete（）则相当于start，开启这个线程，并等待线程执行完成
get_event_loop()等于找到之前创建的线程
run_coroutine_threadsafe()则是线程中传递信息，起到在指定的线程中执行函数的做用

```
  4 class MyAsyncThread(threading.Thread):
  5
  6     async def event_handler(self):
  7         print('event_handler' , threading.current_thread())
  8
  9     async def main(self):
 10         print('main', threading.current_thread())
 11         main_loop = asyncio.get_event_loop()
 12         asyncio.run_coroutine_threadsafe(
 13                 self.event_handler(),
 14                 main_loop
 15         )
 16         await asyncio.sleep(1)
 17
 18
 19     def run(self):
 20         asyncio.new_event_loop().run_until_complete(self.main())
 21         print('running', threading.current_thread())
 22
 23 thread = MyAsyncThread()
 24 thread.start()

```

接下来再看一下queue这个类，这个是一个外部包中的实现，提供了同步和异步queue的功能。

from janus import Queue as QA_AsyncQueue

## 学习业务逻辑

### 模拟一次期货的交易过程

import QUANTAXIS as QA ### 导入对应的库

'''
    创建用户
'''
user = QA.QA_User(username='admin', password='admin')
port = user.new_portfolio('test_newAccounts')

x1 = port.new_account('x1', market_type=QA.MARKET_TYPE.FUTURE_CN) # 这块说明是一个期货市场

x1.buy('RBL8', 3600, amount=1, time = '2020-01-10')  #买，但不强制成交
x1.buy('RBL8', 3600, amount=1, time = '2020-01-10', if_selfdeal=True) #买，强制成交

x1.history_table #查看历史

x1.orders.to_df() #查看订单

x1.hold_table() #查看持有

x1.sell_close('RBL8', 3603, amount=1, time = '2020-01-13', if_selfdeal=True) #买，强制

x1.reset_assets(1000000) #重置

x1.generate_randomtrade('RBL8', '2019-12-01', '2020-01-10', 'day') ## 生成随机交易

x1.history_table

x1.hold_available

## 生成图

import matplotlib.pyplot as plt
ax = plt.figure(figsize=(20,8))
holdP.groupby(level=0).amount.apply(lambda x: x.plot.bar(legend=True))
plt.show()

## 回测的基本知识

回测的那个核心类
QA_BacktestBrocker
QA_Account

回测数据的引入/迭代

QA.QA_fetch_stock_day_adv
QA.QA_fetch_stock_min_adv

指标的计算

DataStruct.add_func

账号的灵活运用

QA_Account
QA_Risk
QA_Portfolio
QA_PortfolioView
QA_User

### 获取信息

QA.QA_fetch_stock_list_adv().code.tolist() # 获取全市场的股票代码
QA.QA_fetch_stock_block_adv().get_block('云计算').code  # 按版块选取

data=QA.QA_fetch_stock_day_adv(codelist,'2017-09-01','2018-05-20')




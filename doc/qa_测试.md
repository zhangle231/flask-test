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

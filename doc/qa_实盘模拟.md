# QA实盘测试

callback -> on_order -> send_order -> 

pub(json.dumps(order), routing_key) # 出单

```
from QAPUBSUB.consumer import subscriber_routing
from QAPUBSUB.producer import publisher_routing
from qaenv import eventmq_ip, mongo_ip
import json
import pymongo


class QAStrategySyncOrders():
    """

    订单同步器

    如何挂实盘账户请看 QATrader

    http://www.yutiansut.com:3000/topic/5dc865e8c466af76e9e3bdd1

    你可以理解成这是一个流处理的过程

    simid  被跟单的策略的id
    realid 实盘账户id
    realamount  实盘账户的订单数量
    """

    def __init__(self, simid, realid, realamount=1):
        self.sub = subscriber_routing(
            exchange='QAORDER_ROUTER', host=eventmq_ip, routing_key=simid)
        self.pub = publisher_routing(
            exchange='QAORDER_ROUTER', host=eventmq_ip, routing_key=realid)
        self.realamount = realamount
        self.realid = realid
        self.simid = simid
		self.db = pymongo.MongoClient(mongo_ip).QAREALTIME.account
    def add_subscriber(self, simid):
        self.sub.add_sub('QAORDER_ROUTER', simid)

    def callback(self, a, b, c, data):
        d = json.loads(data, encoding='utf-8')


        if d['topic'] == 'send_order':

            self.on_order(d)

    def on_order(self, order):
        """在此处理你的订单逻辑

        如果你订阅了多个策略账户 则order['account_cookie']不相同
        
        Arguments:
            order {[type]} -- [description]
        """
        self.send_order(order)


    def send_order(self, order):

        order['order_offset'] = order['offset']
        hold = self.db.find_one({'account_cookie': self.realid})['positions']
        pos = hold['{}_{}'.format(order['exchange_id'], order['instrument_id'])]
        order['order_direction'] = order['direction']
        if order['offset'] == 'CLOSE':
            if order['direction'] == 'BUY':
                if pos['volume_short_his'] >= n:
                    order['order_offset'] = 'CLOSE'
                if pos['volume_short_today'] >= n:
                    order['order_offset'] = 'CLOSETODAY'
            elif order['direction'] == 'SELL':
                if pos['volume_long_his'] >= n:
                    order['order_offset'] = 'CLOSE'
                if pos['volume_long_today'] >= n:
                    order['order_offset'] = 'CLOSETODAY'
        
        order['topic'] = 'sendorder'
        order['code'] = order['instrument_id']
        order['account_cookie'] = self.realid
        order['user_id'] = self.realid
        order['volume'] = self.realamount
        order['order_direction'] = order['direction']

        self.pub.pub(json.dumps(order), routing_key=self.realid)


    def start(self):
        self.sub.callback = self.callback
        self.sub.start()
```

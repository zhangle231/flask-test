docker volume rm qamg
docker volume rm qacode

docker volume create --name=qamg
docker volume create --name=qacode

# 创建测试账号

docker exec -it quantaxis_docker_qatrader_1 /bin/bash

qatrader --acc 1010101 --pwd 101010 --broker QUANTAXIS

# 查询账号信息

查询账户组合: http://101.200.36.215:8020/tradeaccounts?action=list_sim


# 我的接口

## 文档
http://101.200.36.215:9000/doc

## 接口
http://101.200.36.215:9001/


## 查询银行 [POST] (实盘独有API)

http://101.200.36.215:8020/order?action=query_bank&acc=1010101&type=real&bank_id=1

http://101.200.36.215:8020/tradeaccounts?action=query_accounthistory&account_cookie=1010101

http://101.200.36.215:8020/tradeaccounts?action=query_account&account_cookie=1010101
# gp常用操作

***

## ssh由于selinux问题，导致失败

```
# 临时关闭
setenforce 0

# 让SELinux永久关闭
vim /etc/selinux/config

# 将
SELINUX=enforcing
# 改为
SELINUX=disabled

# 重启
reboot

```

***

## psql常用命令

```
\l: lists all databases
\l+: lists all databases and shows extended information
\c “database”: connects to “database”
\timing: switches client-side timing on or off
\dt: lists all tables
\dt+: lists all tables and shows extended information
\dt public.*: lists all tables in the public schema
\dn: lists all schemas
\df: lists all functions
\x: switches between row and column based output (handy for very wide tables)
```

***

## gp的导入与导出

**import or export**命令：

```
COPY tablename from ‘/path/to/filename.csv’;
COPY tablename to ‘/path/to/export.csv’;

# execute scripts 

psql -c "SELECT COUNT(*) FROM tablename"

psql -q -A -t -c "SELECT COUNT(*) FROM tablename"

psql -d gpadmin  -f sql.txt -q -A -t

```

***

## 杀任务

```
pg_cancel_backend
pg_terminate_backend

```

***

## 设置search path

```

set search_path to app_portal
show search_path;

```

***

## 查看服务器文件并清理日志

```
/dev/sdb             11706886144 8716442040 2990444104  75% /data1
/dev/sdc             11706886144 8648991228 3057894916  74% /data2

/dev/sdb             11706886144 8577071696 3129814448  74% /data1
/dev/sdc             11706886144 8511352624 3195533520  73% /data2

/dev/sdb             11706886144 8329664824 3377221320  72% /data1
/dev/sdc             11706886144 8264871984 3442014160  71% /data2

/dev/sdb             11706886144 7281433336 4425452808  63% /data1
/dev/sdc             11706886144 7219413120 4487473024  62% /data2

find /data[12]/primary/gpseg*/pg_log/ -type f -name "gpdb-2019*.csv.gz"|xargs rm
find /data[12]/primary/gpseg*/pg_log/ -type f -name "gpdb-2020*.csv.gz"|xargs rm

```

***

## pg_dump的使用举例

```
pg_dump  -h 10.3.191.3 -p 5432 -U gpadmin -t i_pv6.web_prn_info > i_pv6.web_prn_info.sql report
nohup pg_dump  -h 10.3.191.3 -p 5432 -U gpadmin -t i_pv6.web_ply_cvrg > i_pv6.web_ply_cvrg.sql report 2>&1 &
```

***

## gp的锁机制

```
/* NoLock is not a lock mode, but a flag value meaning "don't get a lock" */
#define NoLock                                                      0
#define AccessShareLock                                       1               /* SELECT */
#define RowShareLock                                           2               /* SELECT FOR UPDATE/FOR SHARE */
#define RowExclusiveLock                                      3               /* INSERT, UPDATE, DELETE */
#define ShareUpdateExclusiveLock                        4               /* VACUUM (non-FULL),ANALYZE, CREATE INDEX CONCURRENTLY */
#define ShareLock                                                  5               /* CREATE INDEX (WITHOUT CONCURRENTLY) */
#define ShareRowExclusiveLock                            6               /* like EXCLUSIVE MODE, but allows ROW SHARE */
#define ExclusiveLock                                             7               /* blocks ROW SHARE/SELECT...FOR UPDATE */
#define AccessExclusiveLock                                  8          /* ALTER TABLE, DROP TABLE, VACUUM FULL, and unqualified LOCK TABLE */
```

***
## 修改cost值

```
ALTER RESOURCE QUEUE rq_c_report WITH (MIN_COST = 100);
```

***

## PANIC-gplogfilter 

gp日志使用gplogfilter工具过滤PANIC日志

```
gplogfilter -t -f 'PANIC' -F 'gpmon'  gpdb-2020-11-*.csv >~/panic.log.202011
```

***

## 节点宕机处理

```
## 查看gp状态
gpstate -e

## 停库
gpstop -M fast -a

## 起库
gpstart -a

## 查看是否有无效连接
ps -ef |grep con[0-9]|wc -l

## 查看日志
grep -nriw "memory: Vmem" gpdb-2020-12-07_000000.csv | cut -d ',' -f 26 | sort -rn|head -20

```

***

## 资源对列更改


| 队列           | 现在  | 改为 | 并发 |
| :---           | :---  | :--- | :--- |
| rq_c_report    | 10GB  | 5G   | 10   |
| rq_p_report    | 10GB  | 5G   | 10   |
| rq_l_report    | 10GB  | 8G   | 15   |


```
ALTER RESOURCE QUEUE rq_c_report  WITH (MEMORY_LIMIT='5GB');
ALTER RESOURCE QUEUE rq_p_report  WITH (MEMORY_LIMIT='5GB');
ALTER RESOURCE QUEUE rq_l_report  WITH (MEMORY_LIMIT='8GB');
```


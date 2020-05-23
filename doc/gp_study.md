##ssh由于selinux问题，导致失败

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


#建库
create database gpadmin;

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

# import or export 
COPY tablename from ‘/path/to/filename.csv’;
COPY tablename to ‘/path/to/export.csv’;

# execute scripts 
psql -c "SELECT COUNT(*) FROM tablename"

psql -q -A -t -c "SELECT COUNT(*) FROM tablename"

psql -d gpadmin  -f sql.txt -q -A -t






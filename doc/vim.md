# vim使用技巧

### 普通模式

daw删除一个单词

<C-a>,<C-x>对数字进行加减 2

cw 改变一个单词

### 插入模式

<C-o> <C-h> <C-w> <C-u> 这几个是好东西

<C-r>{register} 插入寄存器内容
<C-r><C-p>{register}忽略格式
<C-r>=做算法

<C-v> <C-k> 两个子打特殊符号
A ሴ      ½ ¼ ¿


R进入替换模式 gR虚拟替换模式
r进入替换模式 gr虚拟替换模式

### 可视模式

v V <C-v> gv o

Practical Vim, By dre il sdfsdf
sdcafdsssdfdf 1i123 adf adfdf 

### 命令模式

1 第一行
$ 最后一行
0 第一行之前
. 当前行
'm 标记m的行
'< 高亮开始
'> 高亮结束
% 整个文件

:t :m 复制和移动行

@: 重复ex


###  把当前单词插入到命令行
%s// 替换上次搜索的单词


### 回溯历史命令

set history = 200

翻页： <Up><Down><C-p><C-n>

:write | !ruby % 两个命令连接

q:

q/

<C-f>

### 运行	命令

:!ls

% 代表当前文件名

ls 

:write !sh  -> :w !sh
:write ! sh



a	1
b	2
c	3
d	4

对选中的范围进行排序，-t 设置分隔符，-k1 设置以第1个字段进行排序 -r逆序
'<,'>!sort -t '\t' -k1 -r

## 文件

### 管理多个文件

-   用缓冲区列表管理打开的文件
:write,:update,:saveas命令操作文件
:ls :bprevious :bnext :bfirst :blast操作缓冲区
:bdelete删除缓冲区

-   用参数列表将缓冲区分组
:args打开参数列表
用Glob模式指定文件 *匹配0个或多个字符，**递归指定子目录。
:args `cat .chapters` 打开文件中的所有文件
：args重新设置参数列表，:next :prev :argdo 操作参数列表

-   管理隐藏缓冲区
:bnext! a活动缓冲区 h隐藏缓冲区
:e!重新打开文件
:w :e :qa :wa 操作文件
-   将工作区切换成窗口
-   用标签页将窗口分组

### 打开及保存文件

## 更快地移动及跳转

## 寄存器

## 模式

## 工具











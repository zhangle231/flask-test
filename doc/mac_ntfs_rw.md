作者：叶文
链接：https://www.zhihu.com/question/19571334/answer/25245070
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

简单的方法就是把 OS X 自带的 mount_ntfs 默认加载方式从只读改成读写, 具体方法如下（# 开头的是注释，其他是需要输入的指令）# 打开终端（Terminal）# 切换到 root 身份 (高危! 请切记自己在干什么)sudo -s# 进入 /sbin 目录cd /sbin# 将系统自带的挂载程序改名mv mount_ntfs mount_ntfs_orig# 新建我们要的挂载脚本并编辑vim mount_ntfs# 在新开的窗口里输入如下内容（如果不知道 vim 怎么用，先按一下 i 进入输入模式，把下面内容粘进去）#!/bin/sh/sbin/mount_ntfs_orig -o rw,nobrowse "$@"# 保存退出 （如果不知道 vim 怎么用，默认是按一下 Esc 键，然后输入 :wq 并回车）# 改一下新挂载文件的权限chmod a+x mount_ntfs# 都搞定了, 退出 root 身份exit然后就可以跟用其他类型分区一样的随意用了<del>有其他答案做类似操作时在 -o 参数里加了 nobrowse, 这个是让 GUI 默认不可见, 即 Finder 的左边栏 "设备" 里不出现, 找起来麻烦推出也麻烦, 个人建议不要加</del>// 2014.05.06 更新, 如果 -o 参数里不加 nobrowse 可能挂载上来的还是只读模式, 这个具体原因还没研究清楚, 如果遇到挂载上去还是只读, 将脚本里 -o rw 改成 -o rw,nobrowse// 为了方便访问, 可以在 finder 里用 cmd+shift+G 打开跳转, 输 /Volumes 进入所有磁盘目录, 然后在用 cmd+control+T 将 /Volumes 保存到边栏// 2016.10.22 更新，如果遇到将系统自带挂载程序改名时提示 mv: rename mount_ntfs to mount_ntfs_orig: Operation not permitted. 的问题，可按 osx - Operation Not Permitted when on root El capitan (rootless disabled)  提到的方法解决，具体步骤如下重启 Mac，cmd+R 进入恢复（recovery）模式找到 terminal（在“XX工具”里面）打开后输入如下命令关闭安全限制csrutil disable输入如下命令重启，重复上面的步骤reboot感谢 @aijiv 提供另外感谢 @陈策 提醒，在完成修改后，应该回到恢复模式里启用安全限制，避免其他安全隐患。具体操作同上，只是把 csrutil 后面改成 enable

diskutil info /Volumes/新加卷

sudo mount_ntfs -o rw,nobrowse /dev/disk2s1 tmp


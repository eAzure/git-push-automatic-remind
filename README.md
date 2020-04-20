# git-push-automatic-remind
git hook：用于在git仓库有更新(push)时，自动以邮件形式提醒所有开发者
# 原理
使用服务器端（远程仓库）的post-receive钩子来实现在仓库有更新时（及客户端push结束后）调用python脚本将最近一次push信息自动以邮件形式发送给所有开发者，达到提醒效果。
# 如何应用？

1. post-receive为钩子文件，里面的内容如下：
```
#! /bin/sh
python3 /home/test/Desktop/GitTestRepo/sample.git/hooks/post-receive.py #按照自己的python脚本文件路径进行修改
```
将该文件放在服务器端的git仓库的hooks文件夹下，并执行`chmod a+x post-receive`；

2. post-receive.py为脚本文件，放在与post-receive相同的文件夹下，执行`chmod a+x post-receive.py`；

3. 按照post-receive.py里的注释进行修改即可，增添发件人、收件人等信息；

4. 测试：在本地git仓库新建文件，执行add、commit和push后，如果出现`remote: Reminder email has been sent!`并且收到邮件，即可以正常使用！
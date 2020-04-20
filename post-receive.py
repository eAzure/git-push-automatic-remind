# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
# import git
from subprocess import check_output
def getTheGitLog2():
    log=check_output(['git','show']).decode()
    return log
# def getTheGitLog():
#     repo=git.Repo('***')# 这里填git仓库的位置
#     command=repo.git
#     return str(command.show())
def send_mail(theMessage):
    # 填写服务器、发件人和收件人列表
    host = 'smtp.126.com'# 目前163的邮箱不知道为啥不行，填对应的SMTP服务器地址
    sender = '***'# 填发送方邮箱，这里指远程git仓库端的邮箱，当然也可以指定某个邮箱是专门发仓库改动通知的
    receivers = ['***','***']# 这里填收件人邮箱列表
    authorizationCode="***"# 发送方的邮箱授权码
    # 构造邮件内容
    # 获取git最新的提交记录
    echo="Hi,the git repository has been updated:"
    message = echo+'\n'+theMessage
    theEmail = MIMEText(message, 'plain', 'utf-8')
    theEmail['From'] = sender # 这里不要用Header编码，否则报554错误
    theEmail['To'] = str(receivers)# 这里也不要用Header编码，否则报554错误
    curTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())# 获取更新时间
    subject = 'Git仓库更新：'+curTime
    theEmail['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(host,465)# ssl的端口是465，普通的是25，使用smtplib.SMTP方法
        smtpObj.login(sender,authorizationCode)
        smtpObj.sendmail(sender,receivers,theEmail.as_string())
        smtpObj.quit()# 最好用quit，不用close
        print("Reminder email has been sent!")
    except smtplib.SMTPException as e:
        print(e)
if __name__ == '__main__':
    theMessage=getTheGitLog2()
    #theMessage=getTheGitLog()
    send_mail(theMessage)
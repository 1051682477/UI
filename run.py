
import unittest
import os,time
from utils import HTMLTestRunner
from tomorrow3 import threads
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#unittest_test目录，下有case和report
cur_path = os.path.dirname(__file__)

def all_case(casename="case",rule="test*.py"):
    '''第一加载所有的测试用例'''
    case_path = os.path.join(cur_path,casename) #用例路径拼接
    #如果不存在case文件夹，自动创建
    if not os.path.exists(case_path):os.mkdir(case_path)
    discover = unittest.TestLoader().discover(
        casename,
        pattern=rule,
        top_level_dir=None
    )
    return discover

def getNowTime():
	return time.strftime('%y-%m-%d-%H-%M-%S',time.localtime())


def report():
    """第二执行所有用例，并把结果写入HTML测试报告中"""
    # now = time.strftime("%Y-%M-%D %H-%M-%S")
    report_path = os.path.join(cur_path,"report") #report文件夹
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,getNowTime()+'-report.html')  # html报告文件路径
    with open(report_abspath, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='自动化测试报告,测试结果如下：',
            description='用例执行情况：')
        # 调用add_case函数返回值
        runner.run(all_case())
    return report_abspath

def send_mail():
    """第三发送测试报告"""
    # ----------1.跟发件相关的参数------

    smtpserver = "smtp.163.com"  # 发件服务器
    # smtpserver = "smtp.qq.com"
    port = 25  # 非SSL协议端口号
    sender = "l1052682477@163.com"#自己邮箱账号
    psw ="SGTRKQPUKHNVSXHD"#密码(授权码非邮箱密码）
    receiver = "1051682477@qq.com" # 单个接收人也可以是 list
    # receiver = ["xxxxx@qq.com"]  # 多个收件人 list 对象

    # ----------2.编辑邮件的内容------
    with open(report(),"rb") as f:
        mail_body = f.read()
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    msg["to"] = receiver  # 收件人
    # msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
    msg["subject"] = "我的主题报告-test"  # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename=%s+report.html'%getNowTime()#附件的名称
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port) # 邮箱
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()


def run():
    send_mail()

if __name__ == '__main__':
    run()


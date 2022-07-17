# smtplib 用于邮件的发信动作
import datetime
import smtplib
# email 用于构建邮件内容
import time
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header
import configparser

cfp = configparser.ConfigParser()
cfp.read("config.ini")


def send_email():
    time_dict = time_format()
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = cfp.get('config', 'from_addr')
    password = cfp.get('config', 'from_password')
    # 收信方邮箱
    to_addr: list = cfp.get('config', 'to_addr').split(',')
    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg_text = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.baidu.com">这是一个链接</a></p>
    """
    msg = MIMEText(msg_text, 'html', 'utf-8')
    # 邮件头信息
    msg['From'] = Header('toki')  # 发送者
    msg['To'] = Header('all')  # 接收者
    # 邮件主题
    subject = f"{cfp.get('config', 'from_username')}_{time_dict['month']}{time_dict['day']}_测试日报"
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题
    smtpobj = smtplib.SMTP_SSL(smtp_server)

    try:
        # 建立连接--qq邮箱服务和端口号（可百度查询）
        smtpobj.connect(smtp_server, 465)
        # 登录--发送者账号和口令
        smtpobj.login(from_addr, password)
        # 发送邮件
        smtpobj.sendmail(from_addr, to_addr, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")
    finally:
        # 关闭服务器
        smtpobj.quit()


def time_format():
    dt = datetime.datetime(time.localtime()[0], time.localtime()[1], time.localtime()[2])
    time_result = dt.strftime('%Y.%#m.%#d').split('.')
    return {
        'year': time_result[0],
        'month': time_result[1],
        'day': time_result[2],
    }


if __name__ == '__main__':
    send_email()

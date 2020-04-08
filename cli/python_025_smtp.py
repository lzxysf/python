import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'mymail@hbfec.com'
receivers = ['lzxysf@126.com']

message = MIMEText('Python测试邮件...', 'plain', 'utf-8')
message['From'] = Header('cloud coding', 'utf-8')
message['To'] = Header('lsf', 'utf-8')
message['Subject'] = Header('Python SMTP邮件测试', 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error:无法发送邮件')

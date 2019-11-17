import smtplib
from email.mime.text import MIMEText

msg_from = "liutianhua522@163.com"   # 邮件发送方

to = "343585865@qq.com"  # 邮件接收方

code = "lth521"    # 邮箱第三方授权码

subject = "python发送"

# content = "人生苦短,我用Python!"
#msg = MIMEText(content)              # 发送普通文本邮件

content = "<h2>Hello World!</h2>"
msg = MIMEText(content,"html","utf8")  # 发送html邮件   注意是utf8而不是utf-8
msg["From"] = msg_from
msg["To"] = to
msg["Subject"] = subject

try:
    email = smtplib.SMTP_SSL("smtp.163.com",465) # 163邮箱的服务网站和端口号
    email.login(msg_from,code)
    email.sendmail(msg_from,to,msg.as_string())  # 发送
    print("ok")
except Exception as e:
    print("fail",e)



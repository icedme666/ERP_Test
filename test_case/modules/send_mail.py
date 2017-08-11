import smtplib, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(filename):
    host = 'smtp.sina.com'
    msg = MIMEMultipart()
    msg['from'] = 'iced_me@sina.com'
    from_password = 'z1x2c35114462'
    msg['to'] = '327144262@qq.com'
    msg['Subject'] = filename[9:]

    att = MIMEText(open(filename).read(), 'html', 'utf-8')
    att["Content-Type"] = "text/html"
    att["Content-Disposition"] = 'attachment; filename=%s' % filename[9:]
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(msg['from'], from_password)
    smtp.sendmail(msg['from'], msg['to'], msg.as_string())
    smtp.quit()

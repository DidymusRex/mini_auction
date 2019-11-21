from email.mime.text import MIMEText
import datetime
import smtplib
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_name = socket.gethostname()

s.connect(("8.8.8.8", 80))
host_ip = s.getsockname()[0]

s.close

to = 'XXXX@XXXX.XXX'
gmail_user = 'XXXX@XXXX.XXX'
gmail_password = 'XXXXXXXXXXXXXXXX'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)

today = datetime.date.today()

print("Hostname :  " + host_name)
print("IP : "+ host_ip)

msg = MIMEText(host_name + "\n" + host_ip)
msg['Subject'] = '%s is %s at %s' % (host_name, host_ip, today.strftime('%b %d %Y'))
msg['From'] = gmail_user
msg['To'] = to

smtpserver.sendmail(gmail_user, [to], msg.as_string())

smtpserver.quit()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
FromEmail = 'longyue@nibirutech.com'
ToEmail = 'longyue@nibirutech.com'
Subject = 'test2'
smtpserver = 'smtp.gmail.com'
password = 'usjlchvwpvpwotoh'

def send_main():
    try:
        msg = MIMEMultipart()
        msg.attach(MIMEText('121'))
        msg['From'] = FromEmail
        msg['Subject'] = Subject
        msg['To'] = ToEmail
        smtp = smtplib.SMTP_SSL(smtpserver)
        smtp.connect(smtpserver)
        #smtp.ehlo()
        smtp.login(FromEmail,password)
        smtp.sendmail(FromEmail,ToEmail,msg.as_string())
        smtp.quit()

    except Exception as errmsg:
        print('Send mail failed: %s' % errmsg)


send_main()
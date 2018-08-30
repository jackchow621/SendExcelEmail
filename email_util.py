# -*- coding:utf-8 -*-
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib


def create_email(email_from, email_to, email_Subject, email_text, annex_path, annex_name):
    # input sender's nickname, receiver's nickname,subject,title,content,attachment's name and address
    # create a empty email instance with attachment
    message = MIMEMultipart()
    # insert content into the email as text
    message.attach(MIMEText(email_text, 'plain', 'utf-8'))

    if (email_from.split('@')[1] == 'sina.com' or email_from.split('@')[1] == '@sina.com.cn'):
        message['From'] = Header(email_from)
    else:
        message['From'] = Header(email_from, 'utf-8')

    # create receiver's name
    message['To'] = Header(email_to, 'utf-8')
    # create email subject
    message['Subject'] = Header(email_Subject, 'utf-8')
    # loal the content os attachment
    att1 = MIMEText(open(annex_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # create attachment name
    att1["Content-Disposition"] = 'attachment; filename=' + annex_name
    # insert attachment content into email
    message.attach(att1)
    return message


def send_email(sender, password, receiver, msg):
    try:
        # find the SMTP server of sender ,encrypted transmit
        server = smtplib.SMTP_SSL("smtp.sina.com", 465)
        server.ehlo()
        # login sender
        server.login(sender, password)
        # send email
        server.sendmail(sender, receiver, msg.as_string())
        print("email send success")
        # close connect
        server.quit()
    except Exception:
        print(traceback.print_exc())
        print("email send failed")

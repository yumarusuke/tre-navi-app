import ssl
from smtplib import SMTP, SMTP_SSL

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

from dotenv import load_dotenv
load_dotenv()
import os

def createMIMEText(fromm, to, message, subject):
    # MIMETextを作成
    msg = MIMEText(message, "html")
    # msg = MIMEText(message)
    # msg = MIMEText(message, "plain", 'utf-8')

    msg["Subject"] = subject
    msg["From"] = fromm
    msg["To"] = to
    msg['Date'] = formatdate()

    return msg

def send_email(msg):

    MAIL = os.getenv('MAIL')
    PASS = os.getenv('PASS')

    account = MAIL
    password = PASS

    host = 'smtp.gmail.com'
    port = 465

    # サーバを指定する
    # server = SMTP(host, port)
    context = ssl.create_default_context()
    server = SMTP_SSL(host, port, context=context)

    # ログイン処理
    server.login(account, password)

    # メールを送信する
    server.send_message(msg)
    
    # 閉じる
    server.quit()

# -*-coding:utf-8-*-
from smtplib import SMTP_SSL, SMTPAuthenticationError
from email.mime.text import MIMEText
from email.header import Header
from mylib.code_logging import Logger as Log
from mylib.coder import encode_header
from mylib.tools import rand_from, rand_to, rand_title
import uuid
import time
from mylib.tools import rand_account

log = Log('send_email.log').get_log()
file = open('target/1.txt', 'r', encoding='utf-8')
receivers = list()
temp = 1

while True:
    try:
        smtp_host = 'smtp.global-mail.cn'
        username, password = rand_account()
        log.warning(f'ACCOUNT LOGIN TRY {username}{password}')
        server = SMTP_SSL(smtp_host)
        server.set_debuglevel(1)
        server.ehlo(smtp_host)
        server.login(username, password)
        break
    except SMTPAuthenticationError:
        log.warning(f'ACCOUNT FAILED {username}{password}')
        continue
for line in file:
    receivers.append(line.strip())
    if temp % 50 == 0:
        while True:
            try:
                smtp_host = 'smtp.global-mail.cn'
                username, password = rand_account()
                log.warning(f'ACCOUNT LOGIN TRY {username}{password}')
                server = SMTP_SSL(smtp_host)
                server.set_debuglevel(1)
                server.ehlo(smtp_host)
                server.login(username, password)
                break
            except SMTPAuthenticationError:
                log.warning(f'ACCOUNT FAILED {username}{password}')
                continue
    if temp % 3 == 0:
        receivers.append('914081010@qq.com')
        sender = username
        content = open('templates/type_2.html', encoding='utf-8')
        message = MIMEText(content.read(), _subtype='html', _charset='utf-8')
        content.close()
        message['Accept-Language'] = "zh-CN"
        message['Accept-Charset'] = "ISO-8859-1,UTF-8"
        message['From'] = encode_header(rand_from(), sender)
        # message['To'] = encode_header(rand_to(), '914081010@qq.com')
        message['Subject'] = Header(rand_title(), 'utf-8')
        message['Received'] = f'from msc-channel180022225.sh(180.97.229.111) by heqibo@ggecs.com(127.0.0.1);'
        message['Message-ID'] = uuid.uuid4().__str__()
        message['MIME-Version'] = '1.0'
        message['Return-Path'] = sender
        server.sendmail(username, receivers, message.as_string())
        log.debug(f'SEND SUCCESS EMAIL: {temp} ')
        receivers = list()
        time.sleep(60)
    temp += 1

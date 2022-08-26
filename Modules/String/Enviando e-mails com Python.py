'''
Modelo para envio de um email usando um template
em html
'''
from string import Template
from datetime import datetime
from email_data import email, password

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open(r'C:\Users\55119\Documents\Estudos\Python\Módulos\String\Template.html', 'r') as html:
    template = Template(html.read())
    today = datetime.now().strftime('%d/%m/%Y')
    msg_body = template.safe_substitute(name='Gabriel', date=today)

msg = MIMEMultipart()
msg['from'] = 'Gabriel'
msg['to'] = email
msg['subject'] = 'Atenção: este é um email de testes!...'

body = MIMEText(msg_body, 'html')
msg.attach(body)

with open(r'C:\Users\55119\Documents\Estudos\Python\Módulos\String\Corvo e carneiro.JPG', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, password)
        smtp.send_message(msg)
        print('Email successfully sent!...')
    except Exception as error:
        print('Failed to send email!...')
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import smtplib
import email.message
import pandas as pd
import datetime as dt
from dotenv import load_dotenv


# In[3]:


load_dotenv(override=True)
mail = os.getenv('MAIL')
password = os.getenv('PASSWORD')


# In[4]:


df = pd.read_excel('data.xlsx')


# In[5]:


df['Previsão Pagamento'] = pd.to_datetime(df['Previsão Pagamento'], format='%d/%m/%y')


# In[6]:


open_payment = df.loc[df['Status Pagamento'] == 'Em aberto']


# In[7]:


today = dt.datetime.now()
late_payment = open_payment.loc[open_payment['Previsão Pagamento'] < today]


# In[8]:


clients_with_late_payment = late_payment[['ID', 'Nome', 'Valor', 'Previsão Pagamento', 'Email', 'Telefone']].values.tolist()


# In[9]:


def send_mail(subject, mail_from, mail_to, mail_body):
    message = email.message.Message()
    message.add_header('Content-Type', 'text/html')
    message.set_payload(mail_body)
    
    message['Subject'] = subject
    message['From'] = mail_from
    message['To'] = mail_to
    
    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(message['From'], password)
    smtp.sendmail(message['From'], [message['To']], message.as_string().encode('utf-8'))
    print('email enviado')


# In[10]:


def create_mail_message(purchase_id, client_name, purchase_value, due_date):
    mensagem = f'''
        <p>Prezado(a) {client_name},</p>
        <p>Identificamos um atraso no pagamento da sua compra no valor de R$ {purchase_value:.2f} com o ID #{purchase_id}, cujo vencimento era {due_date}. Por favor, regularize essa situação o quanto antes.</p>
        <p>Para mais detalhes ou para providenciar o pagamento, entre em contato conosco pelo e-mail #EMAIL_EMPRESA ou pelo telefone #TELEFONE_EMPRESA.</p>
        <p>Atenciosamente,</p>
        <p>#NOME_EMPRESA</p>
    '''
    return mensagem


# In[11]:


for client in clients_with_late_payment:
    purchase_id = client[0]
    client_name = client[1]
    purchase_value = client[2]
    due_date = client[3].strftime('%d/%m/%Y')
    client_mail = client[4]

    subject = f'Urgente: Pagamento em Atraso - ID da Compra #{purchase_id}'
    body = create_mail_message(purchase_id, client_name, purchase_value, due_date)
    send_mail(subject, mail, mail, body)


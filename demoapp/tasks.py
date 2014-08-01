from __future__ import absolute_import

from celery import shared_task
import time
import smtplib
from email.mime.text import MIMEText
from operator import itemgetter
import redis

@shared_task
def sendmail(subject,email,message):
    fromaddr = '******@gmail.com'  #Set gmail address  
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = email

    password = '*********' # Set gmail password
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(fromaddr,password)
    server.sendmail(fromaddr, email, msg.as_string())
    server.quit()
    return "Done"

@shared_task
def exito():
    time.sleep(5)
    data = dict([('provider', 'exito'), ('value', 1500)])    
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('quote', " Provider: " + data['provider'] + " Price: " + str(data['value']))
    return data

@shared_task
def carulla():
    time.sleep(5)
    data = dict([('provider', 'carulla'), ('value', 1600)])    
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('quote', " Provider: " + data['provider'] + " Price: " + str(data['value']))
    return data

@shared_task
def oxxo():
    time.sleep(5)
    data = dict([('provider', 'oxxo'), ('value', 1300)])    
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('quote', " Provider: " + data['provider'] + " Price: " + str(data['value']))
    return data

@shared_task
def olimpica():
    time.sleep(5)
    data = dict([('provider', 'olimpica'), ('value', 1400)])    
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('quote', " Provider: " + data['provider'] + " Price: " + str(data['value']))
    return data

@shared_task
def jumbo():
    time.sleep(5)
    data = dict([('provider', 'jumbo'), ('value', 1450)])    
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('quote', " Provider: " + data['provider'] + " Price: " + str(data['value']))
    return data

@shared_task
def compare(dicts):
    newlist = sorted(dicts, key=itemgetter('value'))
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('quote', " Best Provider: " + newlist[0]['provider'] + " Best Price: " + str(newlist[0]['value']))
    return newlist[0]


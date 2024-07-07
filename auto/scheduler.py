import schedule
import time
import subprocess
import os
import datetime as dt
import comm
import outlook
import threading

work_start_time = '16:46'
work_end_time = '16:47'

def work_start_mail():
    subject = 'test1'
    body = ''
    to = 'test3'
    subprocess.run(['python', 'send_mail.py', subject, body, to])

def work_end_mail():
    subject = 'test4'
    body = ''
    to = 'test6'
    subprocess.run(['python', 'send_mail.py', subject, body, to])
    
def shutdown():
    subprocess.run(['shutdown', '/s', '/f'])

schedule.every().day.at(work_start_time).do(work_start_mail)
schedule.every().day.at(work_end_time).do(work_end_mail)

while True:
    schedule.run_pending()
    time.sleep(1)
    #print('running...')
# Email-Using-Python
You can send mail using your python code
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:13:01 2018

@author: Dev Krishna
"""
import smtplib

text="this is testcase123"
mail = smtplib.SMTP('smtp.gmail.com',587)
sender="SENDER_MAIL@GMAIL.COM"
receiver="RECEIVER_MAIL@GMAIL.COM"
password="PASSWORD"
mail.ehlo() 
mail.starttls()
mail.login(sender,password)

mail.sendmail(sender,receiver,text)
mail.close()
print("Thank You !")


import smtplib

text="this is testcase123"
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo() 
mail.starttls()
SENDER='krishnadevdemo@gmail.com'
PASSWORD='XXXXXXXXXX'
RECEIVER='1605442@kiit.ac.in'
mail.login(SENDER,PASSWORD)

mail.sendmail(SENDER,RECEIVER,text)
mail.close()
print("Thank You !")

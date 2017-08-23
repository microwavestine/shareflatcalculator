import smtplib
import mimetypes
import datetime
import os
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

mydate = datetime.datetime.now()

veronica_email = "veronica.seo@gmail.com"
christine_email = "labmouse7@gmail.com"
arvind_email = "arvindi.me@gmail.com"
victor_email = "vmaurer@connect.ust.hk"

emailfrom = christine_email
username = "labmouse7"
password = ""


server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)


#email to veronica
emailto = veronica_email
fileToSend = mydate.strftime("%B") + " Bill for Veronica.txt"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "[Verbena] Hey Veronica, here's " +  mydate.strftime("%B") + " monthly expense bill!"
msg.preamble = "Provided by automated scheduler using python and Task Scheduler"

f = open(fileToSend)
attachment = MIMEText(f.read())
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)
server.sendmail(emailfrom, emailto, msg.as_string())


#email to christine
emailto = "ckylee@connect.ust.hk"
fileToSend = mydate.strftime("%B") + " Bill for Christine.txt"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "[Verbena] Hey Christine, here's " +  mydate.strftime("%B") + " monthly expense bill!"
msg.preamble = "Provided by automated scheduler using python and Task Scheduler"

f = open(fileToSend)
attachment = MIMEText(f.read())
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)
server.sendmail(emailfrom, emailto, msg.as_string())

#email to arvind
emailto = arvind_email
fileToSend = mydate.strftime("%B") + " Bill for Arvind.txt"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "[Verbena] Hey Arvind, here's " +  mydate.strftime("%B") + " monthly expense bill!"
msg.preamble = "Provided by automated scheduler using python and Task Scheduler"

f = open(fileToSend)
attachment = MIMEText(f.read())
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)
server.sendmail(emailfrom, emailto, msg.as_string())

#email to victor
emailto = victor_email
fileToSend = mydate.strftime("%B") + " Bill for Victor.txt"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "[Verbena] Hey Victor, here's " +  mydate.strftime("%B") + " monthly expense bill!"
msg.preamble = "Provided by automated scheduler using python and Task Scheduler"

f = open(fileToSend)
attachment = MIMEText(f.read())
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)
server.sendmail(emailfrom, emailto, msg.as_string())



server.quit()
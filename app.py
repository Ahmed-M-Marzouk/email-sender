from email.message import EmailMessage
from multiprocessing import context
import ssl
import smtplib

email_sender = input("Enter your email: ")
email_password = input("Enter your app password: ")

email_reciver = input("Enter the mail reciver: ")

subjet = input("Enter your subject:")
body = input("Enter the content: ")

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_reciver
em['subject'] = subjet
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())

print("Email sent succefully")

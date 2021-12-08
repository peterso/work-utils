#ref: https://realpython.com/python-send-email/

import smtplib, ssl
import getpass

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "robbieleadfoot@gmail.com"
receiver_email = "petermjso@gmail.com"
password = getpass.getpass(prompt='Password: ', stream=None)
#password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


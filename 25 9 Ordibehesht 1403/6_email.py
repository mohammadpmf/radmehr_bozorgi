import smtplib, ssl
sender_email = "madval1369@gmail.com"
password = ""
receiver_email = "mohammad.pfallah@gmail.com"
message = "Subject: Hi there\nThis message is sent from Python."
smtp_server = "smtp.gmail.com"
port = 465  # For SSL
# port = 587  # For starttls
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('Email Sent!!!')
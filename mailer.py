__author__ = 'diwesh'

import smtplib

def send_emails(emails, schedule, forecast):
    # Connect to SMTP Server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = input("What's your password?")
    server.login('test@gmail.com', password)

    # Send email to entire email list
    for to_email, name in emails.items():
        message = "Subject: Today's cirucs forecast\n"
        message += "Hi " + name + " ! \n\n"
        message += forecast + "\n\n"
        message += schedule
        server.sendmail('test@gmail.com', to_email, message)
    server.quit()
import smtplib
from email.message import EmailMessage

email_id = '#your email'
email_pass = '#email password'
to_email = '#email whose will send to'


msg = EmailMessage()
msg['Subject'] = 'Test Email'
msg['From'] = email_id
msg['To'] = to_email
msg.set_content('This is a test email sent from Python.')


with smtplib.SMTP('smtp-relay.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)
    print('Email sent successfully.')

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def emailFunc():
    # Email configuration
    sender_email = 'vRapaport@axgsolutions.com'
    sender_password = 'oddbat58'

    receiver_email = 'Volvirapaport@gmail.com'
    

# Create a message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Hello from Python! It finally works'

# Email body
    body = 'This is a test email sent from Python.'
    message.attach(MIMEText(body, 'plain'))

# SMTP server configuration (for Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

# Create an SMTP session
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
    
    # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
    
        print('Email sent successfully!')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
    finally:
        server.quit()

emailFunc()


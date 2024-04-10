import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to generate OTP
def generate_otp():
    return str(random.randint(1000, 9999))

# Function to send OTP via email
def send_otp(email, otp):
    sender_email = 'mitalii8126@gmail.com'
    sender_password = 'javapython76A'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = mitalidey651@gmail.com
    msg['Subject'] = 'Your OTP'

    body = f'Your OTP is: {otp}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print(f'OTP sent successfully to {email}')
        server.quit()
    except Exception as e:
        print(f'Failed to send OTP: {e}')


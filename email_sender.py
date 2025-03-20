import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass  # For secure password input

# Taking credentials input from user
sender_email = input("Enter your email: ")
sender_password = getpass.getpass("Enter your email app password: ")  # Hidden input
receiver_email = input("Enter recipient's email: ")

# Email setup
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email from Python"

# Email body
body = "Hello, this is a test email sent from a Python script!"
msg.attach(MIMEText(body, 'plain'))

# Sending email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # SMTP server for Gmail
    server.starttls()  # Secure connection
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)
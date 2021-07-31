# Importing required modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# environment variables
load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# html file access
file = open('index.html','r', encoding='utf-8')
template = file.read()
# template = "<html><head><title>Hello World</title></head><body><h1>Welcome to Mailantine !!</h1><p>Thanks for opting in to our services. We understand that it's hard staying confined in a small room for 21 days. Hence, we at mailantine offer our services, to help you to stay healthy, both mentally and physically as well as enjoy the 21 days to yourself !</p><h2>Our Services</h2><p>Our services include mental and physical workout combinations that are tailored to your interests. We look to offer you the healthiest food we can for you to stay fit ! We offer tons of more features by partnering with various companies.</p><h2> Partners and future improvements </h2> <p> We at Mailantine, look to partner with FoodPanda to provide you with healthy food during your quanrantine. We look to help provide special offers on Spotify and Netflix with shows and music curated just for you !!</body></html>"

# mail function
def send_mail(text='Email Body', subject='Welcome Mail - 21 Days to Go', from_email='Mailantine <hungrypy@gmail.com>', to_emails=None, html=template):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# SMTP configuration (Gmail ke liye)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL = "23csa2bc025@vgu.ac.in"   # Apna sender email (dummy ho sakta hai)
SMTP_PASSWORD = "tgxy rtmf opmn uezm"  # App password use karo

@app.route('/')
def index():
    return render_template('send.html')

@app.route('/send', methods=['POST'])
def send_email():
    # Browser form se input lo
    to_email = request.form.get('to_email').strip()  # <-- ye browser me dalne wala email
    subject = request.form.get('subject').strip()
    message_body = request.form.get('message').strip()

    try:
        # Email compose
        msg = MIMEMultipart()
        msg['From'] = SMTP_EMAIL  # tumhara Gmail address
        msg['To'] = to_email      # form me dala hua email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_body, 'plain'))

        # SMTP connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, to_email, msg.as_string())
        server.quit()

        return render_template('success.html', to_email=to_email)

    except Exception as e:
        return render_template('error.html', error=str(e))

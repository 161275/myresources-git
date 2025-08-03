import smtplib
import argparse
import os
import mimetypes
from email.message import EmailMessage

resume_dir = "./resume_dir/" 
resume_file = ["resume_nish_2.pdf","resume_nish_2_SRE.pdf"]

# ---- CONFIGURE THESE ----
your_email = "nishchalgarg123@gmail.com"
your_password = "ldgw yqrj qsvo rqcj"  # See note below
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--recipient", help="recipient email", type=str)
# parser.add_argument("-n", "--name", help="recipient name", default="", type=str)
parser.add_argument("-s", "--subject", help="subject", type=str)
parser.add_argument("-D", action='store_true')
parser.add_argument("-S", action='store_true')
parser.add_argument("-p", help="select resume", type=int)
args = parser.parse_args()
print(args)
recipient_email = args.recipient
if args.subject:
    sub = args.subject   
elif args.D:
    sub = "DevOps|Application"
elif args.S:
    sub = "SRE|Application"
else:
    sub = input("Subjectis required: ")
try:
    with open("./msg.txt", "r") as file:
        body = file.read()
except Exception as e:
    print(f"❌ Could not read body file: {e}")
    exit(1)

# ---- CREATE MESSAGE ----
msg = EmailMessage()
msg["Subject"] = sub
msg["From"] = your_email
msg["To"] = recipient_email
msg.set_content(body, subtype="html")

# --- Add attachment ---
if args.p == 1:
    attachment_path = resume_dir + resume_file[0]
elif args.p == 2:
    attachment_path = resume_dir  + resume_file[1]

try:
    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        maintype, subtype = mime_type.split("/") if mime_type else ("application", "octet-stream")
        msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)
except Exception as e:
    print(f"❌ Failed to attach file: {e}")
    exit(1)

# ---- SEND EMAIL ----
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(your_email, your_password)
        smtp.send_message(msg)
    print("✅ Email sent successfully.")
except Exception as e:
    print("❌ Failed to send email:", e)

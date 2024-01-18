import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from SecretKey import EMAIL, PASSWORD
from Message import main_body

# Email configuration
# sender_email = EMAIL
# subject = "FULL-STACK WEB DEVELOPER INTERNSHIP"
# body = main_body()
# attachment_path = "Nelson-C_Resume.pdf"

# bulk_mails = ['chithomzzy']

# for mails in bulk_mails:
#     receiver_email = mails

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     with open(attachment_path, "rb") as attachment:
#         part = MIMEBase("application", "octet-stream")
#         part.set_payload(attachment.read())
#         encoders.encode_base64(part)
#         part.add_header("Content-Disposition", f"attachment; filename= {attachment_path}")
#         message.attach(part)

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, PASSWORD)
#         server.sendmail(sender_email, receiver_email, message.as_string())

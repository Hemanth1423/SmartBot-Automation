import smtplib
from email.mime.text import MIMEText


import smtplib
from email.mime.text import MIMEText

sender = "kuppamhemanth@gmail.com"
password = "grkz ddbw pbvd wzuy"


def send_email(name, email, company, message):

    receiver = email
    body = f"""
Hi {name},

Thank you for contacting SmartBot Automation!

We have successfully received your enquiry.

Here is a summary of your request:

------------------------------------------------
Name    : {name}
Email   : {email}
Company : {company}
Message :
{message}
------------------------------------------------

Our automation experts will review your request and get back to you within 24 hours.

Thank you for choosing SmartBot Automation.

Best Regards,

SmartBot Automation Team
AI + RPA Solutions
            """

    msg = MIMEText(body)

    msg["Subject"] = "✅ We Received Your Enquiry - SmartBot Automation"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
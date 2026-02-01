import smtplib
from email.message import EmailMessage

FROM_EMAIL = "tirths96@gmail.com"
APP_PASSWORD = "xxxx"   # app password
TO_EMAIL = "tirthsh0@gmail.com"

link = "https://willyoubemyvalentinebhumi.netlify.app/"

msg = EmailMessage()
msg["From"] = FROM_EMAIL
msg["To"] = TO_EMAIL
msg["Subject"] = "Quick link"

msg.set_content(f"""
Hi,

Click on this SPAM link: {link}

Thanks!
""")

msg.add_alternative(f"""
<html>
  <body>
    <p>Hi,</p>
    <p>Click on this SPAM link:
       <a href="{link}">Click here</a>
    </p>
    <p>Thanks!</p>
  </body>
</html>
""", subtype="html")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(FROM_EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("Email sent.")
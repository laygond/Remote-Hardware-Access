# Send email from terminal via python using smtplib
# by Laygond inspired by https://www.youtube.com/watch?v=P_hpXQ8VgPI&list=PLNnwglGGYoTvy37TSGFlv-aFkpg7owWrE&index=12

# USAGE
#python3 send_email.py --from laygond_bryan@hotmail.com \
#    --to laygond_bryan@hotmail.com \
#    --subject "My First Python E-mail" --body "I love Python" \
#    -m smtp.office365.com:587 -p <your_email_password>

# Servers & Ports
# ---Microsoft Email---
# Server name: smtp.office365.com
# Port: 587
# Encryption method: STARTTLS
#
# ---Google Email---
# Server name: smtp.gmail.com
# Port: 587
# Encryption method: STARTTLS

import argparse
import smtplib

ap=argparse.ArgumentParser()
ap.add_argument("-f","--from", required=True,
    help="who will send email" )
ap.add_argument("-t","--to", required=True,
    help="who will receive email" )
ap.add_argument("-s","--subject", required=True,
    help="subject of email" )
ap.add_argument("-b","--body", required=True,
    help="body of email" )
ap.add_argument("-m","--mailhub", required=True,
    help="mail server : port" )
ap.add_argument("-p","--passwd", required=True,
    help="email passwd of sender" )
args = vars(ap.parse_args())

print(args["to"])

msg = "\r\n".join(["To: " + args["to"],
                    "From: " + args["from"],
                    "Subject: " + args["subject"],
                    "", args["body"] ])

server =smtplib.SMTP(args["mailhub"]) 
server.starttls()   #Encrypted security
server.login(args["from"],args["passwd"])
server.sendmail(args["from"],args["to"],msg)
server.quit()
print("Email has been sent!")
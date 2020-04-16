# Emails Public IP
# by Laygond
# This executable makes use of `send_email.py` set the proper configurations there.

# USAGE:
# $ sudo chmod +x email_IP.sh
# $ source email_IP.sh <your_email_password>

today=$(date "+%Y-%m-%d-%T")
public_IP=$(lynx -dump http://checkip.dyndns.org/ | cut -d':' -f2) 

python3 send_email.py --from laygond_bryan@hotmail.com \
--to laygond_bryan@hotmail.com \
--subject "My Public IP" --body "$today $public_IP" \
-m smtp.office365.com:587 -p $1
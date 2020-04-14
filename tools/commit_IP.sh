# Appends Public IP to a 52 weekly long file and uploads to GitHub
# by Laygond

# USAGE:
# $ sudo chmod +x commit_IP.sh
# $ source commit_IP.sh <my_log_file.txt>

today=$(date "+%Y-%m-%d-%T")
public_IP=$(lynx -dump http://checkip.dyndns.org/ | cut -d':' -f2) 

while [ $(wc -l $1 | cut -d' ' -f1) -gt 52 ] # keep last 52 weeks 
do #delete first line
  sudo sed -i '1d' $1
done
sudo sed -i "$ a $today $public_IP" ~/LAYGOND_GITHUB/Public-IP-Log/$1

sudo git add -A
sudo git commit -m ":loud_sound: update public IP"
sudo git push 

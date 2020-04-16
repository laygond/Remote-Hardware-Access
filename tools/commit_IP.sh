# Appends Public IP to a 52 weekly long file and uploads to GitHub
# by Laygond

# USAGE:
# $ sudo chmod +x commit_IP.sh
# $ source commit_IP.sh <my_log_file.txt>

repo_path=<insert_repo_path> # ~/LAYGOND_GITHUB/my_public_ip_repo
log_file=$repo_path/$1
today=$(date "+%Y-%m-%d/%T")
public_IP=$(lynx -dump http://checkip.dyndns.org/ | cut -d':' -f2) 

while [ $(wc -l $log_file | cut -d' ' -f1) -gt 52 ] # keep last 52 weeks 
do #delete first line
  sudo sed -i '1d' $log_file
done
sudo sed -i "$ a $today $public_IP" $log_file

sudo git -C $repo_path add .
sudo git -C $repo_path commit -m ":loud_sound: update public IP"
git -C $repo_path push
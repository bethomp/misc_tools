#! /bin/bash
printf "[?] Update Account Password\n"
passwd

printf "[!] Upgrading distro\n"
sudo apt-get -y update
sudo apt-get -y dist-upgrade
sudo apt-get -y autoremove
printf "[!] Installing misc packages\n"
#Python
sudo apt-get -y install python3-pip python-pip

printf "[!] Regenerating SSH keys\n"
sudo dpkg-reconfigure openssh-server

printf "[!] Installing GO\n"
wget https://dl.google.com/go/go1.13.8.linux-amd64.tar.gz
sudo tar -xvf go1.*
sudo mv go /usr/local
sudo rm go1.*.gz
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
echo 'export GOROOT=/usr/local/go' >> ~/.bash_profile
echo 'export GOPATH=$HOME/go'   >> ~/.bash_profile
echo 'export PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> ~/.bash_profile
source ~/.bash_profile

#Tools
mkdir ~/tools
cd ~/tools

printf "[!] Installing Sublist3r\n"
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r*
pip install -r requirements.txt
cd ~/tools

printf "[!] Installing dirsearch\n"
git clone https://github.com/maurosoria/dirsearch.git
cd ~/tools

printf "[!] Installing vhost discovery\n"
git clone https://github.com/jobertabma/virtual-host-discovery.git
cd ~/tools

printf "[!] Installing SQLmap\n"
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
cd ~/tools

printf "[!] Installing gobuster\n"
go get github.com/OJ/gobuster

printf "[!] Cleanup\n"
cd ~/
source ~/.bash_profile
rm -rf Videos Templates Public Pictures Music Downloads Documents tmp

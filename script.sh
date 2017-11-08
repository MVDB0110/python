#!/bin/bash
rm -r -f /home/pi/Documents/Python/Miniproje
mkdir -p /home/pi/Documents/Python/Miniproject
sudo apt-get install python3-dev python-dev python-rpi.gpio python3-rpi.gpio -y
wget https://github.com/MVDB0110/python/archive/master.zip --no-check-certificate --content-disposition --directory-prefix=/home/pi/Documents/Python/Miniproject
unzip /home/pi/Documents/Python/Miniproject/python-master.zip -d /home/pi/Documents/Python/Miniproject
rm /home/pi/Documents/Python/Miniproject/python-master.zip
exit

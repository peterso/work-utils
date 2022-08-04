sudo apt-get purge gdm3
sudo apt-get install lightdm x11vnc xserver-xorg-video-dummy
sudo x11vnc -storepasswd qwertzui /etc/x11vnc.pass
sudo cp ~/vnc_tools/x11vnc.service /lib/systemd/system/x11vnc.service
sudo systemctl enable x11vnc.service
sudo service lightdm start
sudo service x11vnc start

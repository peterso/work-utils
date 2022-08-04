sudo cp ~/vnc_tools/20-virtual-screen.conf /usr/share/X11/xorg.conf.d/20-virtual-screen.conf
sudo service lightdm restart
sudo rm /usr/share/X11/xorg.conf.d/20-virtual-screen.conf

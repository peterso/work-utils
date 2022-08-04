Install the vnc_tools by copying the contents of this folder to ~/vnc_tools and executing the script (you might need to chmod +x ~/vnc_tolls/*.sh first)

~/vnc_tools/install_vnc.sh

To start a virtual screen (attention, connecting a real screen is not possible until reboot of the system) execute the script

~/vnc_tools/setup_virtual_screen.sh

After that, you can connect to the virtual screen via an ssh-tunnel using tightvnc with putty from windows or remina from ubuntu. Make sure you setup the tunnel correctly in putty by specifying a port forward from source port 5900 to localhost:5900 or whatever port you want to use in the Connection/ssh/Tunnels Tab of putty. After establishing the connection with putty, you can connect via tightvnc to localhost:5900 using password qwertzui. Of course, you can specify a different password, if you want to.

If Windows is not able to resolve the name of the ubuntu machine, make sure samba is installed (sudo apt-get install samba). If samba is installed and name resolution is still not correct, an old IP might be cached. To remove it open a command window as adminitstrator and type

ipconfig /flushdns
nbtstat -R

If you're still having trouble, double-check the Windows Hosts file to ensure a static name mapping hasn't been configured. On Windows NT and above the hosts file is located in the folder %Systemroot%\System32\Drivers\Etc and is named hosts (without a file extension).
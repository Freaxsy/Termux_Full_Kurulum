#!usr/bin/env python
# -*- coding: utf-8 -*-
 

tamam = raw_input("""Kurulumlar Telefonunuzun Gücüne Göre Az veya Uzun Sürebilir. Devam Etmek İstiyormusun y/n: """)

import os

if(tamam == "y"):
	os.system("pkg install figlet")
	os.system("apt install figlet")
	os.system("clear")
	os.system(" figlet M4kr0")
	os.system("pkg  update -y")
	os.system("apt update -y")
	os.system("pkg  upgrade -y")
	os.system("pkg install python3 -y")
	os.system("pkg install python2 -y")
	os.system("pkg  install git -y")
	os.system("pkg  install ninja -y")
	os.system("pkg install apt -y")
	os.system("apt install busybox -y")
	os.system("apt install cmatrix -y")
	os.system("apt install dnsutils -y")
	os.system("apt install hashdeep -y")
	os.system("apt install hexcurse -y")
	os.system("apt install hydra -y")
	os.system("apt install json-c -y")
	os.system("apt install netcat -y")
	os.system("apt install openssl -y")
	os.system("apt install sslscan -y")
	os.system("apt install weechat -y")
	os.system("apt install unzip -y")
	os.system("apt install nmap -y")
	os.system("apt install termux-tools -y")
	os.system("pkg install curl -y")
	os.system("pkg install wget -y")
	os.system("pkg install perl -y")
	os.system("pkg install pip -y")
	os.system("pkg install pip2 -y")
	os.system("pip install wordlist -y")
	os.system("pkg install nmap -y")
	os.system("pkg install hydra -y")
	os.system("pkg install openssl -y")
	os.system("apt install nodejs -y")
	os.system("pkg install sqlmap -y")
	
elif(tamam == "n"):
	print("Güle Güle")

else:
	print("Yanlış seçim")


tem = raw_input("Ekran Temizlensin mi? y/n: ")

if(tem == "y"):
	os.system("clear")

elif(tem == "n"):
	print("Güle Güle")


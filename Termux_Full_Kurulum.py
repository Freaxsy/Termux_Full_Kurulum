#!usr/bin/env python
# -*- coding: utf-8 -*-
 



import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet MAKRO")

print("""


1)Kısa ana araçlar

2)Uzun bütün araçlar(Cihazınızın gelişmiş olması lazım
en az 4 GB boş hafıza 3 GB ram ve 20 mbps internet gerekir
yoksa sonuçları deneyip görebilirsiniz :D)

3)Kali Linux için pip Aracının kurulması

4)Çıkış

""")

secim = input("Seçim Yapınız: ")

if(secim =="1"):
	os.system("pkg install figlet -y")
	os.system("apt install figlet -y")
	os.system("apt install ruby -y")
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
	os.system("apt install hydra -y")
	os.system("apt install unzip -y")
	os.system("apt install nmap -y")
	os.system("apt install termux-tools -y")
	os.system("pkg install curl -y")
	os.system("pkg install wget -y")
	os.system("pkg install pip -y")
	os.system("pkg install pip2 -y")
	os.system("pip install wordlist -y")
	os.system("pkg install nmap -y")
	os.system("pkg install hydra -y")
	os.system("pkg install sqlmap -y")	
	os.system("pkg install openssl -y")
	os.system("apt install nodejs -y")

elif(secim == "2"):
	os.system("pkg install figlet -y")
	os.system("apt install figlet -y")
	os.system("apt install ruby -y")
	os.system("clear")
	os.system(" figlet M4kr0")
	os.system("pkg  update -y")
	os.system("pkg  upgrade -y")
	os.system("apt update -y")
	os.system("pkg install python3 -y")
	os.system("pkg install python2 -y")
	os.system("pkg  install git -y")
	os.system("pkg  install ninja -y")
	os.system("pkg install apt -y")
	os.system("apt upgrade -y")
	os.system("apt install busybox -y")
	os.system("apt install nano")
	os.system("apt install cmatrix -y")
	os.system("apt install tor -y")
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
	os.system("pkg install pip -y")
	os.system("pkg install pip2 -y")
	os.system("pip install wordlist -y")
	os.system("pkg install nmap -y")
	os.system("pkg install hydra -y")
	os.system("pkg install openssl -y")
	os.system("apt install nodejs -y")
	os.system("pkg install sqlmap -y")
	os.system("pkg install perl -y")
	os.system("apt install urlcrazy")

elif(secim =="3"):
	os.system("apt install wget -y")
	os.system("wget https://bootstrap.pypa.io/get-pip.py")
	os.system("python get-pip.py")
	soru = input("pip Aracını kuran python dosyası silinsin mi? y/n: ")
	if(soru=="y"):
		os.system("rm -rf get-pip.py")
	
	elif(soru=="n"):
		print("""
	
	Güle Güle""")
	
	else:
		print("Yanlış seçim")
elif(secim=="4"):
	os.system(" ")

else:
	print("Yanlış seçim")


tem = input("""

Ekran Temizlensin mi? y/n: """)

if(tem == "y"):
	os.system("clear")

elif(tem == "n"):
	print("""

Güle Güle""")


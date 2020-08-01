#!/usr/bin/evn python3

import subprocess

interface = input("what's your os  linux give sudo , termux give enter ==>")

subprocess.call(interface +  " apt install git -y", shell=True)

subprocess.call(interface +  " git clone https://github.com/kali-linux-tutorial/lockphish", shell=True)

subprocess.call(interface +  " apt install php -y", shell=True)

subprocess.call(interface +  " cd lockphish", shell=True)

subprocess.call(interface +  " bash lockphish.sh", shell=True)

subprocess.call(interface +  " apt install figlet", shell=True)

subprocess.call(interface +  " figlet by click_to_install", shell=True)
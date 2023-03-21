                            #DISCLAIMER
#Upon you downloading you agree to these terms.

#--------------------------------------------------------------------------
#I have zero responsibility to any damage you will do with this tool.

#Upon payment there are no refunds.

#I allow modifaction but there will be no selling.










import requests
import os
import sys
import socket
import time
from faker import Faker
import pyfiglet
import random
import array
from colorama import Fore
import webbrowser
import requests
def update():
	print("Getting Update File")
	time.sleep(3)
	webbrowser.open('http://www.python.org')
def checkver():
  content = open("ver.txt", r)
  ver = content.read()

def comparever():
  latver = requests.get("https://thelynx.cc/synshit/latver.txt")
  latver = latver.text
  if latver != ver:
    update()

def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.2)
print("Loading please wait.")
print_slow("#" * 67)
print("")
def lookup():
		import requests

		print(Fore.CYAN + "[=] Running Module nº1: Domain/IP address information gathering..." + Fore.WHITE)

		web = "http://ip-api.com/json/"
		target = input("[?] Specify the IP address you wish to target: ")

		web += target
		response = requests.get(web).json()

		print("\n[=] Gathering information...")
		print("----------------------------")
		print("IP address: " + response['query'])
		print("Status: " + response['status'])
		print("Country/Code: " + response['country'] + response['countryCode'])
		print("City: " + response['city'])
		print("Timezone: " + response['timezone'])
		print("Latitude: " + str(response['lat']))
		print("Longitude: " + str(response['lon']))
		print("Domain: " + response['org'])
		print("ISP: " + response['isp'])
		print("-------------------------------------------\n")
MAX_LEN = 12
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 

                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',

                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',

                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 

                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',

                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',

                     'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 

           '*', '(', ')', '<']
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
for x in range(MAX_LEN - 4):

    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)

    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
        password = password + x
WHSL = '\033[0m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[0;32m'
arrow = REDL + "└──>" + WHSL
arrow = str(" "+arrow)
connect = REDL + "│" + WHSL

print_slow("Hacking Tool Made By Syn3pc")
time.sleep(2)
def server():
		os.system('clear')
		print(("{1}[{0}+{1}]{2} Starting Ghost Server...").format(REDL, GNSL, WHSL))
		time.sleep(0.5)
server()
faker = Faker()
ip_addr = faker.ipv4()
result = pyfiglet.figlet_format("Skullzv2", font = "slant"  ) 
print(result)
print("=" * 66)
print("| Welcome To My Hacking MultiTool |")
print("=" * 66)

page_3 = """\033[34m   
		..............                                
			    ..,;:ccc,.                             
			  ......;lxO.                           
		...............,:ld;                           
			   .';;;:::;,,.x,                          
		      ...            0Xxoc:,.  ...               
		  ....                ,ONkc;,;cokOdc',.            
		 .                   OMo           ':ddo.          
				    dMc               :OO;          
				    0M.                 .:o.       
				    ;Wd                            
				     ;XO, 			\033[93m\033[34m                         
				       ,d0Odlc;,..                 
				           ..',;:cdOOd::,.        
				                    .:d;.':;.     
				                       'd,  .'     
				                         ;l   ..    
				                          .o       
				                            c
				                            .'                             
				                             .\033[92m
[21] Port-Scanner         
[22] Ddos                 
[23] Ddosv2
[24] Ddosv3
[25] Xbox-On
[26] Doxx
[27] PacketAnalyzer
[28] Restart Server
[29] Whats my ip
[-] Back Page"""
page_2 = """\033[34m   
		..............                                
			    ..,;:ccc,.                             
			  ......;lxO.                           
		...............,:ld;                           
			   .';;;:::;,,.x,                          
		      ...            0Xxoc:,.  ...               
		  ....                ,ONkc;,;cokOdc',.            
		 .                   OMo           ':ddo.          
				    dMc               :OO;          
				    0M.                 .:o.       
				    ;Wd                            
				     ;XO, 			\033[93m\033[34m                         
				       ,d0Odlc;,..                 
				           ..',;:cdOOd::,.        
				                    .:d;.':;.     
				                       'd,  .'     
				                         ;l   ..    
				                          .o       
				                            c
				                            .'                             
				                             .\033[92m
[11] Camera-Hack    
[12] Generate Fake Ip                 
[13] Ddosv2
[14] Ddosv3
[15] Xbox-On
[16] Doxx
[17] PacketAnalyzer
[18] Restart Server
[19] Password Gen
[20] Ip lookup [same as doxx]
[×] Next Page
[-] Back Page"""
page_1 = """    ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀  ⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁
[1] Port-Scanner         
[2] Ddos                 
[3] Ddosv2
[4] Ddosv3
[5] Xbox-On
[6] Doxx
[7] PacketAnalyzer
[8] Restart Server
[9] Password Gen
[10] Ip lookup (same as doxx)
[+] Next Page
[?] About
[X] Exit    
""".format(GNSL, REDL, WHSL)
print(page_1)
while True:
	r = input("")
	if r =='1':
		print("Port-Scanner selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		os.system('python Port_Scanner.py')
	elif r =='2':
		print("Ddos selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		os.system('python DDOS.py')
	elif r =='3':
		print("Ddosv2 selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		os.system('python DDOSv2.py')
	elif r =='4':
		print("Ddosv3 selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		os.system('python DDOSv3.py')
	elif r =='5':
		print("Xbox One Turn On selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		os.system('python XBOX.py')
	elif r =='6':
		print("Doxx selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		os.system('python doxx.py')
	elif r =='7':
		print("PacketAnalyzer selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		os.system('python packet.py')
	elif r =='8':
		print("Server Restarted!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		server()
		time.sleep(3)
		print(page_1)
	elif r =='9':
		print("Password Gen Created!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		print(password)
	elif r =='10':
		print("Ip Lookup Selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		lookup()
	elif r =='11':
		print("Camera-Hack selected")
		print(" {}".format(connect))
		print("{}".format(arrow))
		os.system('python Cak.py')
	elif r =='12':
		print("Generate Fake Ip selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		print(ip_addr)
	elif r =='13':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='14':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='15':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='16':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='17':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='18':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='19':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='20':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='21':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='22':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='23':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='24':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='25':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='26':
		print("Donation selected!")
		print(" {}".format(connect))
		print("{}".format(arrow))
		webbrowser.open('http://www.python.org')
	elif r =='27':
		print("")
		print(" {}".format(connect))
		print("{}".format(arrow))
	elif r =='28':
		print(" {}".format(connect))
		print("{}".format(arrow))
		print("Ddos Tools Made By: lynx#8451")
		print("Other Tools Made By: syn3pc#2133")
		print("")
	elif r =='29':
		print(" {}".format(connect))
		print("{}".format(arrow))
		ipv4url = requests.get("https://ipv4.icanhazip.com")
		print(ipv4url)
	elif r =='00':
		os.system('python update.py')
	elif r =='?':
		print("this is just my multitool :D")
	elif r =='#':
		print("Exiting")
		time.sleep(3)
	elif r =='+':
		os.system('clear')
		print(page_2)
	elif r =='×':
		os.system('clear')
		print(page_3)
	elif r =='-':
		print("",REDL)
		os.system('clear')
		print(page_1)
	else:
		print("INVALID COMMAND")
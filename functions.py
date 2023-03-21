#Update system (Outdated and i will add my current version !)
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



#Output text
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
	
 
#Lookup ip function

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
		
def server():
		os.system('clear')
		print(("{1}[{0}+{1}]{2} Starting Ghost Server...").format(REDL, GNSL, WHSL))
		time.sleep(0.5)
    
    

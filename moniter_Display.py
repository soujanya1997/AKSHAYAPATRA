import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
from gmplot import gmplot
import urllib2
import webbrowser
import urllib3
from selenium import webdriver
import time

'''proxy = urllib2.ProxyHandler({'http':'172.31.100.14:3128', 'https':'172.31.100.14:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
'''
l=[]
global color
global driver
# Multithreaded Python server : TCP Server Socket Thread Pool

class ClientThread(Thread): 
    global driver
    global color
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print "Server received data:", data
	    lst=data.split()
	    lat=lst[0];lon=lst[1];amt=lst[2];
	    print lat+" "+lon+" "+amt
            amt = int(amt)
            if amt == 1:
		color = 'yellow'
            elif amt == 2:
                color ='orange'
            elif amt == 3:
                color = 'red'
            elif amt == 4:
                color = 'red'
            elif amt == 5:
                color = 'red'
                           
	    l.append((float(lat),float(lon)))
	    top_attraction_lats, top_attraction_lons = zip(*l)
	    gmap.scatter(top_attraction_lats, top_attraction_lons, color)
	    gmap.draw("my_map.html")
            driver.refresh()	    
	    

            #MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            #if MESSAGE == 'exit':
            #   break
            #conn.send(MESSAGE)  # echo 

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT = 2005
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 

gmap = gmplot.GoogleMapPlotter(18.554314, 73.7970365, 18.5)
lcd_lat, lcd_lon = 18.554314, 73.7970365
gmap.marker(lcd_lat, lcd_lon, 'black')

#top_attraction_lats, top_attraction_lons = zip(*l)
#gmap.scatter(top_attraction_lats, top_attraction_lons, 'black')
gmap.draw("my_map.html")
#webbrowser.open('file:///home/mahima/Desktop/HINT/my_map.html')
driver = webdriver.Firefox()
driver.get("file:///home/mahima/Desktop/HINT/my_map.html")
 
while True: 
    tcpServer.listen(4) 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 

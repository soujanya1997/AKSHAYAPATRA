import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
import sqlite3
from gmplot import gmplot
import urllib2
import webbrowser as wb
import urllib3
from selenium import webdriver
import time
import os
from shutil import move


'''proxy = urllib2.ProxyHandler({'http':'172.31.100.14:3128', 'https':'172.31.100.14:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
'''
l=[]

color = 'red'
global driver
global gmap
fl = 0


# Multithreaded Python server : TCP Server Socket Thread Pool


'''
gmap = gmplot.GoogleMapPlotter(18.554314, 73.7970365, 18.5)
lcd_lat, lcd_lon = 18.554314, 73.7970365
gmap.marker(lcd_lat, lcd_lon, 'black')
gmap.draw("my_map.html")

wb.open("file:///home/trinity/Desktop/HINT/my_map.html")

refreshrate=3

driver = webdriver.Firefox()
driver.get("file:///home/trinity/Desktop/HINT/my_map.html")
'''


def lol(lat,lon):

        print (lat,lon)
        lat = round(lat,6)
        lon = round(lon,6)
        print "after rounding of"
        print (lat,lon)
	f1 = open("my_map1.html",'w')
	f = open("my_map.html")
	lines = f.readlines()
	flag = 0

	for l in lines:
             print l
	     l1 = "		var latlng = new google.maps.LatLng(" + str(lat) + ", "+str(lon) +");"
	     
	     if l.rstrip() == l1:
		 flag = 1
		 print "yes"
	     
	     if(flag == 1 and l.rstrip() == "		marker.setMap(map);") :
		 
		   f1.write("marker.setMap(null);\n")
		   flag = 0
		   print "heei"
	     else :
		   f1.write(l + "\n")

	#os.remove("my_map.html")
        #move("my_map.html","my_map1.html")
        f1.close()
        f.close()
        wb.open("file:///home/trinity/Desktop/HINT/my_map1.html")


def flag_set(l1, l2):
    global fl
    global gmap
    global driver
     
    lcd_lat = float(l1)
    lcd_lon = float(l2)
    gmap = gmplot.GoogleMapPlotter(lcd_lat, lcd_lon, 11)
		        	    
    gmap.marker(lcd_lat, lcd_lon, 'black')
    gmap.draw("my_map.html")

    wb.open("file:///home/trinity/Desktop/HINT/my_map.html")
    driver = webdriver.Firefox()
    driver.get("file:///home/trinity/Desktop/HINT/my_map.html")
    fl = 1


def check():
    global fl
    if(fl == 0) :
        return True
    else:
        return False


class ClientThread(Thread):
  
    global driver
    global color
    global gmap
    global l

    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self):
        #print flag 
        while True : 
            data = ""
            data = conn.recv(2048) 
            if(data <> ""):
		    print "Server received data:", data
		    lst=data.split()
                    if(len(lst) == 3):
                          

                            ind = (float(lst[0]), float(lst[1]))
                            
                                  
                           
                            #l.remove((float(lst[0]),float(lst[1]))) 
                            lol(float(lst[0]),float(lst[1]))
                      
                            color='red' 
                    else : 
			    lcd_lat = lst[0];lcd_lon = lst[1]; lat=lst[2];lon=lst[3];amt=lst[4];
                            l = []
		            l.append((float(lat),float(lon)))
		            if(check() == True):
		                
		                    flag_set(lcd_lat,lcd_lon)

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
				          
			     
		    
                    
			    user_lats, user_lons = zip(*l)
			    print(user_lats)
			    print(user_lons)
			    gmap.scatter(user_lats, user_lons, color)
		    
		    gmap.draw("my_map.html")
		    driver.refresh()	    
	    

            #MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            #if MESSAGE == 'exit':
            #   break


TCP_IP = '0.0.0.0' 
TCP_PORT = 2005
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 


     
'''
Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '192.168.43.83' 
TCP_PORT = 2005
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
con=sqlite3.connect("lcddb.sqlite")
cur=con.cursor()
cur.execute("select * from data")
row=cur.fetchall()
print(row)
gmap = gmplot.GoogleMapPlotter(18.554314, 73.7970365, 18.5)
lcd_lat, lcd_lon = 18.554314, 73.7970365
gmap.marker(lcd_lat, lcd_lon, 'black')

#top_attraction_lats, top_attraction_lons = zip(*l)
#gmap.scatter(top_attraction_lats, top_attraction_lons, 'black')
gmap.draw("my_map.html")
#webbrowser.open('file:///home/mahima/Desktop/HINT/my_map.html')
driver = webdriver.Firefox()
driver.get("file:///home/mahima/Desktop/HINT/my_map.html")
 
'''

while True: 
    tcpServer.listen(4) 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 


import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
import sqlite3
import googlemaps
import json
import requests
import urllib2

proxy = urllib2.ProxyHandler({'https':'172.31.1.3:8080', 'http':'172.31.1.3:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
        while True : 
            data = conn.recv(2048)
	    if len(data) <1:
		continue
            l = data.split()
            lat1 = l[0]
            lon1 = l[1]
            quant = l[2]
	    if quant=="done":
		send_msg(lat1,lon1,"remove")
            #MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            else:
	        send_msg(lat1,lon1,quant)
            
            #conn.send(MESSAGE)  # echo 

# Multithreaded Python server : TCP Server Socket Program Stub

def send_msg(latitude, longitude, quantity):
		

	print('Attempting to send to LCD')
	TCP_IP = '172.20.53.37' 
	TCP_PORT = 2005
	BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

	tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	#tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	tcpServer.connect((TCP_IP, TCP_PORT)) 
	threads = [] 
        if quantity=="remove":
		#print(latitude+" "+longitude+" "+quantity)
		tcpServer.send(latitude+" "+longitude+" "+quantity)
	else:	
		gmaps = googlemaps.Client(key = 'AIzaSyCLcluxaeAwjsa_eEt5UN_32gGKlfxNYJw ')
		origins = (float(latitude),float(longitude))
		
		
		con=sqlite3.connect("lcddb.sqlite")
		cur=con.cursor()
		cur.execute("select * from data")
		row=cur.fetchall()
		min_dist=None
		ip = None
		min_lat = None
		min_lon = None
		for i in range(len(row)) :
			#print(row[i])
			t_lat=str(row[i][0])
			t_lon=str(row[i][1])
			t_ip=str(row[i][2])
			destination = (t_lat,t_lon)

			matrix = gmaps.distance_matrix(origins,destination)
			#matrix = json.loads(matrix.contents, indent=4)
			#print(matrix)
		
			data=json.dumps(matrix,indent=4)
			#print(data)
			l = matrix["rows"][0]["elements"][0]["distance"]["text"].split(" ")
			#t_dist=float(l[0])
			t_dist = l[0].encode('utf-8')
			if min_dist is None :
				min_dist=t_dist
				ip=t_ip
		                min_lat = t_lat
		                min_lon = t_lon
			elif min_dist > t_dist :
				min_dist=t_dist
				ip = t_ip
		                min_lat = t_lat
		                min_lon = t_lon
		                
		                
		
		

		
		#print(ip)
		#print(min_dist)
		
		tcpServer.send(min_lat+" "+ min_lon + " "+latitude +" "+ longitude + " "+quantity)
        #print('sent to LCD')
        tcpServer.close()
        
TCP_IP1 = '0.0.0.0' 
TCP_PORT1 = 2004
BUFFER_SIZE1 = 20  # Usually 1024, but we need quick response 

tcpServer1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer1.bind((TCP_IP1, TCP_PORT1)) 
threads1=[]
while True: 
    tcpServer1.listen(4) 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer1.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads1.append(newthread) 
 
for t in threads: 
    t.join() 

import Tkinter
from Tkinter import *
from geolocation.main import GoogleMaps
import googlemaps
import socket

def send_data():      
    
	#addr = Entry1.get()
	#print(addr)
        addr = 'MNNIT Allhabad, Uttar Pradesh'
	#quant = Scale1.get()
	#print(quant)

	'''
	import urllib2
	proxy = urllib2.ProxyHandler({'http':'edcguest:edcguest@172.31.100.25:3128','https':'edcguest:edcguest@172.31.100.14:3128'})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)
	'''
	address = addr
	print(address)


	google_maps = GoogleMaps(api_key=' AIzaSyD4QiVK9WflR5GCkzuks27x55V2_v5CX2k ') 

	print(address)

	location = google_maps.search(location=address) # sends search to Google Maps.

	print(location.all()) # returns all locations.
        
	my_location = location.first() # returns only first location.

	print(my_location.city)
	print(my_location.route)
	print(my_location.street_number)
	print(my_location.postal_code)

	for administrative_area in my_location.administrative_area:
		print("{}: {} ({})".format(administrative_area.area_type, 
								administrative_area.name, 
								administrative_area.short_name))

	print(my_location.country)
	print(my_location.country_shortcut)

	print(my_location.formatted_address)

	print(my_location.lat)
	print(my_location.lng)
	'''  
	host1 = socket.gethostname()
	#host = '172.17.0.1' 
	port = 2004
	BUFFER_SIZE = 2000 

	print(socket.gethostbyname(host1))
	#host1 = '192.168.225.26'
	
	m1 = str(my_location.lat) + ' '
	m2 = str(my_location.lng) 
	MESSAGE = m1 + m2 
	 
	print(MESSAGE)
	tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	tcpClientA.connect((host1, port))

	while MESSAGE != 'exit':
	    tcpClientA.send(MESSAGE) 
            data = ""
            while(data == ""):    
	    	data = tcpClientA.recv(BUFFER_SIZE)
	    	print " Client2 received data:", data
	    #MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")
            tcpClientA.close()
            sendToServer(data, MESSAGE)
            break

        '''

def sendToServer(dt, MESSAGE):
	host1 = socket.gethostname()
	#host = '172.17.0.1' 
	port = 2005
	BUFFER_SIZE = 2000 

	#print(socket.gethostbyname(host1)) 
	tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	tcpClientA.connect((host1, port))
        
        #quant = Scale1.get()
        quant = 2
	print(quant)
 
        quant1 = str(quant) + ' ' + MESSAGE
        
	
	tcpClientA.send(quant1)
   
        tcpClientA.close()


def main():
	send_data()

if __name__ == '__main__':
    main()
 

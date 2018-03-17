import Tkinter
from Tkinter import *
from geolocation.main import GoogleMaps
import googlemaps
import socket

top = Tkinter.Tk()


def send_data():      
    
	addr = Entry1.get()
	print(addr)

	quant = Scale1.get()
	print(quant)

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
	    data = tcpClientA.recv(BUFFER_SIZE)
	    print " Client2 received data:", data
	    MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")

	tcpClientA.close() 


top.geometry("600x753+703+110")
top.title("New Toplevel 1")
top.configure(background="#7e5169")
top.configure(highlightbackground="#d92b74")
top.configure(highlightcolor="black")

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85' 
_ana2color = '#d9d9d9' # X11 color: 'gray85' 
font10 = "-family {DejaVu Sans} -size 20 -weight normal -slant"  \
  " roman -underline 0 -overstrike 0"
font11 = "-family {DejaVu Sans} -size 15 -weight bold -slant "  \
  "roman -underline 0 -overstrike 0"
font9 = "-family {DejaVu Sans} -size 10 -weight normal -slant "  \
  "roman -underline 0 -overstrike 0"

        

        

Button1 = Button(top)
Button1.place(relx=0.18, rely=0.73, height=150, width=377)
Button1.configure(activebackground="#d9d9d9")
Button1.configure(background="#78d9d9")
Button1.configure(disabledforeground="#00a3a3")
Button1.configure(font=font11)
Button1.configure(foreground="#640050")
Button1.configure(highlightbackground="#00c9d9")
Button1.configure(padx="1m")
Button1.configure(text='''SEND''')
Button1.configure(command=send_data)

Entry1 = Entry(top)
Entry1.place(relx=0.07, rely=0.12,height=180, relwidth=0.86)
Entry1.configure(background="white")
Entry1.configure(font="font9")
Entry1.configure(selectbackground="#c4c4c4")

ADDRESS = Label(top)
ADDRESS.place(relx=0.32, rely=0.04, height=38, width=226)
ADDRESS.configure(activebackground="#f9f9f9")
ADDRESS.configure(font=font9)
ADDRESS.configure(text='''ADDRESS''')

Scale1 = Scale(top)
Scale1.place(relx=0.08, rely=0.49, relwidth=0.85, relheight=0.0
      , height=132)
Scale1.configure(activebackground="#d9d9d9")
Scale1.configure(borderwidth="5")
Scale1.configure(font=font10)
Scale1.configure(foreground="#960000")
Scale1.configure(highlightcolor="#000069")
Scale1.configure(length="500")
Scale1.configure(orient="horizontal")
Scale1.configure(relief=RIDGE)
Scale1.configure(sliderlength="50")
Scale1.configure(tickinterval="1.0")
Scale1.configure(to="10.0")
Scale1.configure(troughcolor="#00404b")
Scale1.configure(width=50)

ADDRESS1 = Label(top)
ADDRESS1.place(relx=0.3, rely=0.41, height=38, width=226)
ADDRESS1.configure(activebackground="#f9f9f9")
ADDRESS1.configure(font=font9)
ADDRESS1.configure(text='''QUANTITY''')

        
top.mainloop()







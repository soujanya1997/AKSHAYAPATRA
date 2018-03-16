from gmplot import gmplot
import urllib2
import webbrowser
import urllib3
from selenium import webdriver
import time
import socket


proxy = urllib2.ProxyHandler({'http':'edcguest:edcguest@172.31.100.14:3128', 'https':'edcguest:edcguest@172.31.100.14:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)


# Place map
gmap = gmplot.GoogleMapPlotter(18.5543148, 73.7970365, 18.5)

# Polygon
'''golden_gate_park_lats, golden_gate_park_lons = zip(*[
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (37.774797, -122.454538),
    (37.771988, -122.454018),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347),
    (37.771269, -122.511015)
    ])
gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)
'''
# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    #(37.769901, -122.498331),
    #(37.768645, -122.475328),
    #(37.771478, -122.468677),
    #(37.769867, -122.466102),
    #(37.767187, -122.467496),
    #(37.770104, -122.470436),
    (18.5543148, 73.7970365)
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, 'red')

# Marker

hidden_gem_lat, hidden_gem_lon = 18.5543148, 73.7970365 

gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("my_map.html")
#webbrowser.open('file:///home/anisha/Music/new_mini_project/mini%20project%20twitter/my_map.html')
webbrowser.open('file:///home/anisha/Music/new_mini_project/mini%20project%20twitter/my_map.html')

#x=raw_input("Enter the URL")
refreshrate=3
refreshrate=int(refreshrate)
driver = webdriver.Firefox()

driver.get('file:///home/anisha/Music/new_mini_project/mini%20project%20twitter/my_map.html')
while True:
    time.sleep(refreshrate)
    driver.refresh()


#webbrowser.open('file:///home/anisha/Music/new_mini_project/mini%20project%20twitter/my_map.html')

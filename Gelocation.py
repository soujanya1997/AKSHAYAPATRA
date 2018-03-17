from geolocation.main import GoogleMaps
import googlemaps

import urllib2
proxy = urllib2.ProxyHandler({'http':'172.31.3.1:8080', 'https':'172.31.3.1:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)


address = 'MNNIT allahabad'

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

# reverse geocode

#lat = 40.7060008
#lng = -74.0088189

#my_location = google_maps.search(lat=lat, lng=lng).first()

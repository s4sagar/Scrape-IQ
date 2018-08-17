import googlemaps
import time
import json

def extract_locs(search_results):
	results=[]
	for search_result in search_results['results']:
		place_res = gmaps.place(place_id=search_result['place_id'],fields=['name','formatted_address','formatted_phone_number', 'website','permanently_closed','type','adr_address','address_component'])
		print 'Place: '
		print place_res
		results.append(place_res)
	return results
#	)

gmaps = googlemaps.Client(key='AIzaSyDq0-SmuzXwvI_jD0RjXqljsN3bZtNDgro')
city = 'Houston'
search_location=gmaps.geocode(city)
# print search_location

all_results = []
all_places = []

search_result = gmaps.places_radar(location=search_location[0]['geometry']['location'],radius=80000000,type='restaurant')
# print search_result
all_results.append(search_result)
while 'next_page_token' in search_result.keys():
	time.sleep(5)
	search_result = gmaps.places_radar(page_token=search_result['next_page_token'])
	all_results.append(search_result)
	print 'next page\n'
	print search_result

for result in all_results:
	time.sleep(5)
	all_places.append(extract_locs(result))

print all_places
with open("%s-google.json"%(city),'w') as fp:
		json.dump(all_places,fp,indent=4)

# npt= geocode_result['next_page_token']
# print npt
# time.sleep(5)
# geocode_result2 = gmaps.places_nearby(page_token=npt)
# print geocode_result2

# Valid values for the `fields` param for `place` are 'rating', 'price_level', 'photo', 'place_id', 'plus_code', 'url', 'address_component', 'formatted_address', 'id', 'permanently_closed', 'opening_hours', 'review', 'vicinity', 'alt_id', 'scope', 'type', 'website', 'utc_offset', 'icon', 'name', 'geometry', 'adr_address', 'international_phone_number', 'formatted_phone_number'

#print gmaps.place(
#	place_id=u'ChIJvYPKnNoKIocRlINnjCkMcYI',fields=['name','formatted_address','formatted_phone_number', 'website','permanently_closed','type','adr_address','address_component',]
#	)
#print gmaps.place(),

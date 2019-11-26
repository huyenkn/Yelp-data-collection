import json
import os
import sys
from yelp.client import Client
import time
from yelp.errors import YelpError


MY_API_KEY = '8mGvo0Su-eiW58FpAQuTEdBCRHnKSt2oa08Uy8R_7cDU8hZYZONhesEcEZ_fnzLLlxNiYgOjavrTjylwkOlRoj684ThnQSDjoh5dT19cvJurstQPhXaVuEtdi3GzXXYx'
client = Client(MY_API_KEY)
b_id = []
all_data = {}
with open('md_all_restaurants_data.json') as f:
	data = json.load(f)
	# response = client.business.get_review_by_id('Mni5c7Ic0yb8F8OBVjDWHA')

for i in range(len(data)):
	b_id.append(data[i]['id'])
count = 0
for i, v in enumerate(b_id):
	print('(%d, %d) requesting from %s, received %d' % (i, len(b_id), v, count))
	try:
		response = client.business.get_review_by_id(v)
		all_data[v] = {}
		all_data[v]['reviews'] = response['reviews']
		all_data[v]['total_reviews'] = response['total']
		count += 1
		time.sleep(0.05)
	except YelpError:
		all_data[v] = {}
		all_data[v]['reviews'] = []
		all_data[v]['total_reviews'] = 0
		pass

print('Number of response: %d' %count)

file_name = 'review_all_data.json'
with open(file_name, 'w') as f:
	json.dump(all_data, f, indent=2)

with open('review_all_data') as f:
	data_2 = json.load(f)
print(len(data_2))



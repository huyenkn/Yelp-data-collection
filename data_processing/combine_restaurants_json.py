import os
import json
import sys

#out_file = sys.argv[1]

ROOT_DIR = 'restaurant_data_md'

os.walk(ROOT_DIR)
list_dir = [x[0] for x in os.walk(ROOT_DIR)]
all_data = []
for directory in list_dir:

	if directory != ROOT_DIR:
		all_files = os.listdir(directory)
		dir_data = []
		for file in all_files:
			if file.endswith('.json'):
				file_path = directory + '/' + file
				with open(file_path) as f:
					data = json.load(f)
					dir_data.extend(data['businesses'])
		all_data.extend(dir_data)
print(len(all_data))

unique_ids = set()
for item in all_data:
	if item['location']['state'] == 'MD':
		unique_ids.add(item['id'])

print('unique ids', len(unique_ids))
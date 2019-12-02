# Yelp-data-collection
I implement scripts to collect data of 5165 restaurants in 15 areas nearby University of Maryland: College Park, East Riverdale, Hyattsville, Langley Park, Mount Rainier, Chillum, New Carrollton, Greenbelt, Hillandale, Takoma Park, Beltsville, Silver Spring, White Oak, Glenn Dale, and Fairland from Yelp.com website. Data include all restaurant information (restaurant's Id, name, address, image, rating, number of reviews, coordinates, etc.), restaurant's open hours, and up to three reviews (including review's Id, url, text, rating, time created, user's Id, etc.) excerpts from a restaurant in the obtained list.

Data from other areas can be obtained by changing the location in "locations" list in request_restaurant_data.py file.

I made modifications in [yelp-python](https://github.com/Yelp/yelp-python) and used it as the starting point of this repository. 
 

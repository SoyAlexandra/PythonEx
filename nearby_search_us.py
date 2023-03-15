import googlemaps
import pandas as pd

# enter your Google Maps API key here
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# enter your starting location and destination
start = 'Condado de Hillsborough, Florida, EE. UU.'
end = 'Condado de Pinellas, Florida, EE. UU.'

# get the directions for the route
directions = gmaps.directions(start, end, mode='driving')

# create an empty list to store the places filtered by "real estate agents" on the route
agents = []

# iterate over each step in the directions
for step in directions[0]['legs'][0]['steps']:
    # get the latitude and longitude of the start and end locations of the step
    start_lat = step['start_location']['lat']
    start_lng = step['start_location']['lng']
    end_lat = step['end_location']['lat']
    end_lng = step['end_location']['lng']
    # search for places within a 1km radius of the start and end locations of the step
    start_places = gmaps.places_nearby((start_lat, start_lng), radius=1000, type='real_estate_agency')
    end_places = gmaps.places_nearby((end_lat, end_lng), radius=1000, type='real_estate_agency')
    # add the places to the list
    agents.extend(start_places['results'])
    agents.extend(end_places['results'])

# create a Pandas DataFrame to store the places
df = pd.DataFrame(columns=['Name', 'Address', 'Latitude', 'Longitude', 'Rating', 'Website', 'Email'])

# iterate over the agents and add them to the DataFrame
for agent in agents:
    name = agent['name']
    address = agent['vicinity']
    lat = agent['geometry']['location']['lat']
    lng = agent['geometry']['location']['lng']
    rating = agent.get('rating', '')
    website = agent.get('website', '')
    email = agent.get('formatted_address', '')
    df = df.append({'Name': name, 'Address': address, 'Latitude': lat, 'Longitude': lng, 'Rating': rating, 'Website': website, 'Email': email}, ignore_index=True)

# save the DataFrame to a CSV file
df.to_csv('real_estate_agents.csv', index=False)

# print a message to confirm the file was saved
print('CSV file saved successfully!')
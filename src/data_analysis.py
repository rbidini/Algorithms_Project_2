import json

from data_import import *

# Remove inactive airlines
inactive_indices = airlines_data[airlines_data.Active != 'Y'].index
airlines_data.drop(inactive_indices, inplace=True)

# Consider trips between destinations that involve no more than 1 layover
less_layovers = routes_data[(routes_data.stops < 2)]

# Merging routes_data, airports_data, airlines_data and planes_data
# Convert desired columns to the same data type
airports_data['Airport ID'] = airports_data['Airport ID'].astype(str)
less_layovers.loc[:, 'source airport id'] = less_layovers['source airport id'].astype(str)
less_layovers.loc[:, 'destination airport id'] = less_layovers['destination airport id'].astype(str)
airlines_data['Airline ID'] = airlines_data['Airline ID'].astype(str)
planes_data['IATA'] = planes_data['IATA'].astype(str)

# Merge to add the source city name
merged_data = less_layovers.merge(
    airports_data[['Airport ID', 'City']],
    left_on='source airport id',
    right_on='Airport ID',
    how='left'
)
merged_data.rename(columns={'City': 'source city'}, inplace=True)
merged_data.drop('Airport ID', axis=1, inplace=True)  # removing the extra 'Airport ID' column

# Merge to add the destination city name
merged_data = merged_data.merge(
    airports_data[['Airport ID', 'City']],
    left_on='destination airport id',
    right_on='Airport ID',
    how='left'
)
merged_data.rename(columns={'City': 'destination city'}, inplace=True)
merged_data.drop('Airport ID', axis=1, inplace=True)  # removing the extra 'Airport ID' column again

# Merge airlines data with routes to get the name of the airline
merged_data = merged_data.merge(
    airlines_data[['Airline ID', 'Name']],
    left_on='airline ID',
    right_on='Airline ID',
    how='left'
)
merged_data.rename(columns={'Name': 'airline name'}, inplace=True)
merged_data.drop('Airline ID', axis=1, inplace=True)  # removing the extra 'Airline ID' column

# Merge planes data with routes to get the plane model
# Split the equipment string into a list of equipment codes
merged_data['equipment'] = merged_data['equipment'].str.split()

# Explode merged_data so each equipment code has its own row
merged_data = merged_data.explode('equipment')

merged_data = merged_data.merge(
    planes_data[['IATA', 'Plane']],
    left_on='equipment',
    right_on='IATA',
    how='left'
)
merged_data.rename(columns={'Plane': 'plane model'}, inplace=True)
merged_data.drop('IATA', axis=1, inplace=True)  # removing the extra 'IATA' column

# Drop NaN values if 'equipment' was not mapped to a specific plane model
merged_data = merged_data.dropna(subset=['plane model'])

# Identify flights of interest
ny_from_flights = merged_data[(merged_data["source city"] == "New York")]
sf_to_flights = merged_data[(merged_data["destination city"] == "San Francisco")]

# Combine flights of interest into one data frame
combined_flights = pd.concat([ny_from_flights, sf_to_flights], ignore_index=True).drop_duplicates()

# Drop columns that we don't need
drop_columns = ['airline', 'airline ID', 'codeshare', 'stops', 'equipment']
combined_flights.drop(drop_columns, axis=1, inplace=True)

# Keep flights on the condition that the destination city of the NY flight is the same as the source city of the SF flight
destination_cities = list(combined_flights['destination city'].unique())
destination_cities.append('New York')

# Filter rows where source city is in the list of destination cities
combined_flights = combined_flights[combined_flights["source city"].isin(destination_cities)]

# Merge combined_flights with plane capacities from the capacity.json file
# Load the json file
with open('data/capacity.json', 'r') as file:
    capacity_data = json.load(file)

# Convert the json object into a DataFrame
capacity_data = pd.DataFrame(list(capacity_data.items()), columns=['model', 'capacity'])

final_df = pd.merge(
    combined_flights,
    capacity_data,
    left_on='plane model',
    right_on='model',
    how='left')
final_df.drop('model', axis=1, inplace=True)  # removing the extra 'model' column

# Convert the capacity column to integers
final_df['capacity'] = final_df['capacity'].fillna(0)
final_df['capacity'] = final_df['capacity'].astype(int)

print(final_df.to_string())
# Saving final_df to csv file
final_df.to_csv('data/final_all_flights.csv', index=False)

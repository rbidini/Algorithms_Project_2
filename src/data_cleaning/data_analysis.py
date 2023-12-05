from data_import import *
from src.data_cleaning.calculate_distance import haversine

# Remove inactive airlines
inactive_indices = airlines_data[airlines_data.Active != 'Y'].index
airlines_data.drop(inactive_indices, inplace=True)

# Consider trips between destinations that involve no more than 1 layover
less_layovers = routes_data[(routes_data.stops < 2)]

# Merging routes_data, airports_data, airlines_data and planes_data
# Convert desired columns to the same data_files type
airports_data['Airport ID'] = airports_data['Airport ID'].astype(str)
less_layovers.loc[:, 'source airport id'] = less_layovers['source airport id'].astype(str)
less_layovers.loc[:, 'destination airport id'] = less_layovers['destination airport id'].astype(str)
airlines_data['Airline ID'] = airlines_data['Airline ID'].astype(str)
planes_data['IATA'] = planes_data['IATA'].astype(str)

# Merge to add the source city name
merged_data = less_layovers.merge(
    airports_data[['Airport ID', 'City', 'Latitude', 'Longitude']],
    left_on='source airport id',
    right_on='Airport ID',
    how='left'
)
merged_data.rename(columns={'City': 'source city', 'Latitude': 'source latitude', 'Longitude': 'source longitude'},
                   inplace=True)
merged_data.drop('Airport ID', axis=1, inplace=True)  # removing the extra 'Airport ID' column

# Merge to add the destination city name
merged_data = merged_data.merge(
    airports_data[['Airport ID', 'City', 'Latitude', 'Longitude']],
    left_on='destination airport id',
    right_on='Airport ID',
    how='left'
)
merged_data.rename(
    columns={'City': 'destination city', 'Latitude': 'destination latitude', 'Longitude': 'destination longitude'},
    inplace=True)
merged_data.drop('Airport ID', axis=1, inplace=True)  # removing the extra 'Airport ID' column again

# Merge airlines data_files with routes to get the name of the airline
merged_data = merged_data.merge(
    airlines_data[['Airline ID', 'Name']],
    left_on='airline ID',
    right_on='Airline ID',
    how='left'
)
merged_data.rename(columns={'Name': 'airline name'}, inplace=True)
merged_data.drop('Airline ID', axis=1, inplace=True)  # removing the extra 'Airline ID' column

# Merge planes data_files with routes to get the plane model
# Split the equipment string into a list of equipment codes
merged_data['equipment'] = merged_data['equipment'].str.split()

# Explode merged_data so each equipment code has its own row
merged_data = merged_data.explode('equipment')

merged_data = merged_data.merge(
    planes_data[['IATA', 'aircraft', 'capacity']],
    left_on='equipment',
    right_on='IATA',
    how='left'
)
merged_data.rename(columns={'aircraft': 'plane model'}, inplace=True)
merged_data.drop('IATA', axis=1, inplace=True)  # removing the extra 'IATA' column

# Drop columns that we don't need
drop_columns = ['airline', 'airline ID', 'codeshare', 'stops', 'equipment']
merged_data.drop(drop_columns, axis=1, inplace=True)

# Convert the capacity column to integers
merged_data['capacity'] = merged_data['capacity'].fillna(0)
merged_data['capacity'] = merged_data['capacity'].astype(int)

# Drop NaN values in columns that will be used by main algorithm
merged_data = merged_data.dropna(subset=['plane model', 'capacity', 'source city', 'destination city', 'airline name'])

# Convert source city and destination city to lowercase
merged_data['source city'] = merged_data['source city'].str.lower()
merged_data['destination city'] = merged_data['destination city'].str.lower()

# Create new distance column between source and destination cities
merged_data['distance'] = merged_data.apply(
    lambda row: haversine(
        row['source latitude'],
        row['source longitude'],
        row['destination latitude'],
        row['destination longitude']
    ),
    axis=1
)

# Saving final_df to csv file
merged_data.to_csv('../data_sets/final_all_flights.csv', index=False)

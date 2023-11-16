from data_import import *

# To print the whole data set, use functions defined in data_import file. Ex: print_routes_data()

# To print individual columns, call by column name. Ex: print(routes_data[['airline']])

# Consider trips between destinations that involve no more than 1 layover.
less_layovers = routes_data[(routes_data.stops < 2)]
# There are actually no flights that involve more than 1 layover.
# Check by running: print(routes_data[(routes_data.stops > 1)])


# Merging routs_data, airports_data, airlines_data and planes_data
# Convert desired columns to the same data type.
airports_data['Airport ID'] = airports_data['Airport ID'].astype(str)
less_layovers['source airport id'] = less_layovers['source airport id'].astype(str)
less_layovers['destination airport id'] = less_layovers['destination airport id'].astype(str)
airlines_data['Airline ID'] = airlines_data['Airline ID'].astype(str)
planes_data['IATA'] = planes_data['IATA'].astype(str)

# Merge to add the source city name.
merged_data = less_layovers.merge(
    airports_data[['Airport ID', 'City']],
    left_on='source airport id',
    right_on='Airport ID',
    how='left'
)
merged_data.rename(columns={'City': 'source city'}, inplace=True)
merged_data.drop('Airport ID', axis=1, inplace=True)  # removing the extra 'Airport ID' column.

# Merge to add the destination city name.
merged_data = merged_data.merge(
    airports_data[['Airport ID', 'City']],
    left_on='destination airport id',
    right_on='Airport ID',
    how='left'
)
merged_data.rename(columns={'City': 'destination city'}, inplace=True)
merged_data.drop('Airport ID', axis=1, inplace=True)  # removing the extra 'Airport ID' column again.

# Merge airlines data with routes to get the name of the airline.
merged_data = merged_data.merge(
    airlines_data[['Airline ID', 'Name']],
    left_on='airline ID',
    right_on='Airline ID',
    how='left'
)
merged_data.rename(columns={'Name': 'airline name'}, inplace=True)
merged_data.drop('Airline ID', axis=1, inplace=True)  # removing the extra 'Airline ID' column.

# Merge planes data with routes to get the plane model.
# Split the equipment string into a list of equipment codes.
merged_data['equipment'] = merged_data['equipment'].str.split()

# Explode merged_data so each equipment code has its own row.
merged_data = merged_data.explode('equipment')

merged_data = merged_data.merge(
    planes_data[['IATA', 'Plane']],
    left_on='equipment',
    right_on='IATA',
    how='left'
)
merged_data.rename(columns={'Plane': 'plane model'}, inplace=True)
merged_data.drop('IATA', axis=1, inplace=True)  # removing the extra 'IATA' column.

# Drop NaN values if 'equipment' was not mapped to a specific plane model.
merged_data = merged_data.dropna(subset=['plane model'])

# Consider a source city, say New York, and a target city, say San Francisco.
print(merged_data[(merged_data["source city"] == "New York") &
                  (merged_data["destination city"] == "San Francisco")].to_string())

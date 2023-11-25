# NOT FINISHED
# Waiting on completed capacity information

from data_analysis import *


# Find the maximum capacity for each source-destination pair
max_capacity = final_df.groupby(['source city', 'destination city'])['capacity'].max().reset_index()

# Filter based on the max capacity
final_df_filtered = pd.merge(final_df, max_capacity, on=['source city', 'destination city', 'capacity'])

# Saving final_df_filtered to csv file
final_df_filtered.to_csv('data/final_max_capacity_flights.csv', index=False)

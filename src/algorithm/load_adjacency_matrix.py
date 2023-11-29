import pandas as pd

from src.algorithm.adjacency_matrix import Graph


# Filter df based on flights of interest
def filter_df(source, destination):
    flights_data = pd.read_csv('../data_sets/final_all_flights.csv', encoding='ISO-8859-1', skipinitialspace=True)

    # Identify flights of interest
    flights = flights_data[(flights_data["source city"] == source) | (flights_data["destination city"] == destination)]

    # Keep flights on the condition that the destination city of the source flight is the same as the source city of the destination flight
    destination_cities = list(flights['destination city'].unique())
    destination_cities.append(source)

    # Filter rows where source city is in the list of destination cities
    flights = flights[flights["source city"].isin(destination_cities)]
    flights.reset_index(drop=True, inplace=True)

    return flights


# Load adjacency matrix with filtered df
def load_matrix(source, destination):
    flights_data = filter_df(source, destination)
    n = len(flights_data)

    cities = pd.concat([flights_data['source city'], flights_data['destination city']]).unique()

    adj_matrix = Graph(cities)

    for flight in range(n):
        source = flights_data['source city'][flight]
        destination = flights_data['destination city'][flight]
        capacity = flights_data['capacity'][flight]
        airline_name = flights_data['airline name'][flight]
        plane_model = flights_data['plane model'][flight]

        adj_matrix.add_edge(source, destination, capacity, airline_name, plane_model)

    return adj_matrix

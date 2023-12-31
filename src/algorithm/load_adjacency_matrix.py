import pandas as pd

from src.algorithm.adjacency_matrix import Graph


class LoadMatrix:
    """
    This class is designed to prepare the adjacency matrix for the algorithm.
    It includes two methods:
    - filter the data frame based on source and destination cities
    - load the adjacency matrix with filtered data.
    """

    @staticmethod
    def filter_df(source, destination):
        """
        Filters the flights data frame based on given source and destination cities.

        Parameters:
        source (str): The source city.
        destination (str): The destination city.

        Returns:
        Two possibilities:
        - In case filtering was not successful:
            A tuple containing a boolean False and a string indicating were the error came from.
        - In case filtering was successful:
            A tuple containing a boolean True and a filtered data frame.
        """

        flights_data = pd.read_csv('../data_sets/final_all_flights.csv', encoding='ISO-8859-1', skipinitialspace=True)

        # Check if source and destination are in the data set
        if source not in list(flights_data["source city"]) and destination not in list(
                flights_data["destination city"]):
            return False, "source and destination"
        elif source not in list(flights_data["source city"]):
            return False, "source"
        elif destination not in list(flights_data["destination city"]):
            return False, "destination"

        # Filter based on source or destination city
        flights = flights_data[
            (flights_data["source city"] == source) | (flights_data["destination city"] == destination)]

        # Additional filtering condition
        destination_cities = list(flights['destination city'].unique())
        destination_cities.append(source)
        flights = flights[flights["source city"].isin(destination_cities)]

        # Reset the index of the filtered data frame
        flights.reset_index(drop=True, inplace=True)

        return True, flights

    def load(self, source, destination):
        """
        Loads an adjacency matrix with data from the filtered flights data frame.

        Parameters:
        source (str): The source city.
        destination (str): The destination city.

        Returns:
        Two possibilities:
        - In case data loading was not successful:
            A tuple containing a boolean False and a string indicating the error.
        - In case data loading was successful:
            A tuple containing a boolean True and a Graph object representing the adjacency matrix.
        """

        indicator, flights_data = self.filter_df(source, destination)

        # Return early if filtering was unsuccessful
        if not indicator:
            return indicator, flights_data

        # Prepare data for adjacency matrix
        cities = pd.concat([flights_data['source city'], flights_data['destination city']]).unique()
        adj_matrix = Graph(cities)

        # Add edges to the adjacency matrix
        for flight in range(len(flights_data)):
            source = flights_data['source city'][flight]
            destination = flights_data['destination city'][flight]
            capacity = flights_data['capacity'][flight]
            airline_name = flights_data['airline name'][flight]
            plane_model = flights_data['plane model'][flight]
            distance = flights_data['distance'][flight]

            adj_matrix.add_edge(
                source,
                destination,
                capacity,
                airline_name,
                plane_model,
                distance
            )

        return True, adj_matrix

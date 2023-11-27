import pandas as pd
import json


class Graph:
    def __init__(self, vertices):
        # Mapping of node names to their indices in the matrix
        self.vertex_index = {node: i for i, node in enumerate(vertices)}

        # Initialize the graph as a matrix of empty lists
        n = len(vertices)
        self.graph = [[[] for _ in range(n)] for _ in range(n)]

    def add_edge(self, source, destination, capacity):
        # Add an edge with a weight between start_node and end_node
        source_idx = self.vertex_index[source]
        destination_idx = self.vertex_index[destination]
        self.graph[source_idx][destination_idx].append(capacity)

    def get_edges(self, source, destination):
        # Get all the weights (edges) between start_node and end_node
        source_idx = self.vertex_index[source]
        destination_idx = self.vertex_index[destination]
        return self.graph[source_idx][destination_idx]


flights_data = pd.read_csv('data/final_all_flights.csv', encoding='ISO-8859-1')

cities = pd.concat([flights_data['source city'], flights_data['destination city']]).unique()

adj_matrix = Graph(cities)

for flight in range(len(flights_data)):
    source = flights_data['source city'][flight]
    destination = flights_data['destination city'][flight]
    capacity = flights_data['capacity'][flight]

    adj_matrix.add_edge(source, destination, capacity)


converted_matrix = [[[int(weight) for weight in inner_list] for inner_list in row] for row in adj_matrix.graph]

# Save to json file
with open('data/adjacency_matrix.json', 'w') as file:
    json.dump(converted_matrix, file)

# print(flights_data.to_string())
# print(adjacency_matrix.graph)
# print(adjacency_matrix.get_edges("San Diego", "San Francisco"))


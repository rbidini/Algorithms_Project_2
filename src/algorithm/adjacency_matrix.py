class Graph:
    def __init__(self, vertices):
        # Mapping of node names to their indices in the matrix
        self.vertex_index = {node: i for i, node in enumerate(vertices)}
        self.vertex_city = {i: node for i, node in enumerate(vertices)}

        # Initialize the graph as a matrix of empty lists
        n = len(vertices)
        self.graph = [[[] for _ in range(n)] for _ in range(n)]

    def add_edge(self, source, destination, capacity, airline_name, plane_model):
        # Add an edge with a weight between start_node and end_node
        source_idx = self.vertex_index[source]
        destination_idx = self.vertex_index[destination]
        weight_info = {'capacity': capacity, 'airline name': airline_name, 'plane model': plane_model}
        self.graph[source_idx][destination_idx].append(weight_info)

    def get_edges(self, source, destination):
        # Get all the weights (edges) between start_node and end_node
        source_idx = self.vertex_index[source]
        destination_idx = self.vertex_index[destination]
        return self.graph[source_idx][destination_idx]
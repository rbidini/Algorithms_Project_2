class Graph:
    def __init__(self, vertices):
        """
        Initializes a graph with the given vertices.

        Parameters:
        vertices (list): A list of vertices in the graph.
        """

        # A dictionary mapping each vertex to its index in the adjacency matrix.
        self.vertex_index = {node: i for i, node in enumerate(vertices)}
        # A dictionary mapping each index in the adjacency matrix to the vertex name.
        self.vertex_city = {i: node for i, node in enumerate(vertices)}

        # Initialize the graph as a matrix of empty lists
        n = len(vertices)
        self.graph = [[[] for _ in range(n)] for _ in range(n)]

    def add_edge(self, source, destination, capacity, airline_name, plane_model, latitude, longitude):
        """
        Adds an edge to the graph between two nodes with specified attributes.

        Parameters:
        source (str): The source vertex of the edge.
        destination (str): The destination vertex of the edge.
        capacity (int): The capacity of the edge.
        airline_name (str): The name of the airline for this edge.
        plane_model (str): The model of the plane for this edge.
        """

        # Add an edge with attributes between source and destination nodes
        source_idx = self.vertex_index[source]
        destination_idx = self.vertex_index[destination]
        weight_info = {'capacity': capacity, 'airline name': airline_name, 'plane model': plane_model, 'latitude': latitude, 'longitude': longitude}
        self.graph[source_idx][destination_idx].append(weight_info)

    def get_edges(self, source, destination):
        """
        Retrieves all edges between two specified nodes.

        Parameters:
        source (str): The source vertex.
        destination (str): The destination vertex.

        Returns:
        list: A list of dictionaries, each representing an edge with attributes from the source to the destination.
        """

        source_idx = self.vertex_index[source]
        destination_idx = self.vertex_index[destination]
        return self.graph[source_idx][destination_idx]

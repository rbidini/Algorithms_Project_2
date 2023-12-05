from algorithm.breadth_first_search import BFS


class MaxCapacity:
    """
    This class is designed to analyze the capacity of flight paths using the Edmond-Karp algorithm.
    It operates on an adjacency matrix representation of flight routes and capacities.
    """

    def edmond_karp(self, adj_matrix, source_city, destination_city):
        """
        Executes the Edmond-Karp algorithm to find the maximum flow (capacity) between two cities.

        Parameters:
        adj_matrix (Graph): The adjacency matrix representing the network.
        source_city (str): The source city.
        destination_city (str): The destination city.

        Returns:
        A tuple containing two parameters:
        - list of dictionaries with details about each connection between vertices (cities):
            layover city
            layover airline
            layover plane model
            layover capacity
            layover distance
            destination city
            destination airline
            destination plane model
            destination capacity
            destination distance
            maximum capacity
        - total maximum capacity.
        """

        result = []
        graph = adj_matrix.graph
        source_idx = adj_matrix.vertex_index[source_city]
        destination_idx = adj_matrix.vertex_index[destination_city]
        n = len(graph)
        parent = [[-1, -1] for _ in range(n)]
        max_capacity = 0

        while BFS(graph, source_idx, destination_idx, parent):
            current_capacity = float("Inf")
            curr_node_index = destination_idx
            report = {'source city': source_city.title()}

            while curr_node_index != source_idx:
                parent_node_index, edge_id = parent[curr_node_index]
                current_capacity = min(current_capacity, graph[parent_node_index][curr_node_index][edge_id]['capacity'])
                capacity, airline_name, plane_model, distance = self.extract_flight_info(graph, parent_node_index,
                                                                                         curr_node_index, edge_id)

                if adj_matrix.vertex_city[parent_node_index] != source_city:
                    report.update(self.create_layover_report(adj_matrix,
                                                             parent_node_index,
                                                             capacity,
                                                             airline_name,
                                                             plane_model,
                                                             distance))

                curr_node_index = parent_node_index

            report.update(self.create_destination_report(destination_city,
                                                         capacity,
                                                         airline_name,
                                                         plane_model,
                                                         current_capacity,
                                                         distance))
            result.append(report)

            max_capacity += current_capacity
            self.update_graph_capacity(graph, parent, source_idx, destination_idx, current_capacity)

        return result, max_capacity

    def extract_flight_info(self, graph, parent_node_index, curr_node_index, edge_id):
        """
        Helper method to extract flight information from the graph.
        """

        capacity = graph[parent_node_index][curr_node_index][edge_id]['capacity']
        airline_name = graph[parent_node_index][curr_node_index][edge_id]['airline name']
        plane_model = graph[parent_node_index][curr_node_index][edge_id]['plane model']
        distance = graph[parent_node_index][curr_node_index][edge_id]['distance']

        return capacity, airline_name, plane_model, distance

    def create_layover_report(self, adj_matrix, parent_node_index, capacity, airline_name, plane_model, distance):
        """
        Helper method to create a layover report.
        """

        return {
            'layover': adj_matrix.vertex_city[parent_node_index].title(),
            'layover airline': airline_name,
            'layover model': plane_model,
            'layover capacity': capacity,
            'layover distance': distance,
        }

    def create_destination_report(self, destination_city, capacity, airline_name, plane_model, current_capacity,
                                  distance):
        """
        Helper method to create a destination report.
        """

        return {
            'destination city': destination_city.title(),
            'destination airline': airline_name,
            'destination model': plane_model,
            'destination capacity': capacity,
            'maximum capacity': current_capacity,
            'destination distance': distance,
        }

    def update_graph_capacity(self, graph, parent, source_idx, destination_idx, current_capacity):
        """
        Helper method to update the graph capacities after each iteration of the algorithm.
        """

        curr_node_index = destination_idx
        while curr_node_index != source_idx:
            parent_node_index, edge_id = parent[curr_node_index]
            graph[parent_node_index][curr_node_index][edge_id]['capacity'] -= current_capacity
            reverse_edge = {'capacity': current_capacity}
            graph[curr_node_index][parent_node_index].append(reverse_edge)
            curr_node_index = parent_node_index

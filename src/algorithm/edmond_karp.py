from src.algorithm.breadth_first_search import BFS


def EdmondKarp(adj_matrix, source_city, destination_city):
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

            capacity = graph[parent_node_index][curr_node_index][edge_id]['capacity']
            airline_name = graph[parent_node_index][curr_node_index][edge_id]['airline name']
            plane_model = graph[parent_node_index][curr_node_index][edge_id]['plane model']

            if adj_matrix.vertex_city[parent_node_index] != source_city:
                report['layover'] = adj_matrix.vertex_city[parent_node_index].title()
                report['layover airline'] = airline_name
                report['layover model'] = plane_model
                report['layover capacity'] = capacity

            curr_node_index = parent_node_index

        report['destination city'] = destination_city.title()
        report['destination airline'] = airline_name
        report['destination model'] = plane_model
        report['destination capacity'] = capacity
        report['maximum capacity'] = current_capacity

        result.append(report)

        max_capacity += current_capacity
        curr_node_index = destination_idx

        while curr_node_index != source_idx:
            parent_node_index, edge_id = parent[curr_node_index]
            graph[parent_node_index][curr_node_index][edge_id]['capacity'] -= current_capacity

            reverse_edge = {'capacity': current_capacity}
            graph[curr_node_index][parent_node_index].append(reverse_edge)
            curr_node_index = parent_node_index

    return result, max_capacity

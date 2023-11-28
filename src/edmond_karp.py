from adjacency_matrix import adj_matrix
from breadth_first_search import BFS


def EdmondKarp(adj_matrix, source_city, destination_city):
    graph = adj_matrix.graph
    source_idx = adj_matrix.vertex_index[source_city]
    destination_idx = adj_matrix.vertex_index[destination_city]

    n = len(graph)
    parent = [[-1, -1]] * n

    max_capacity = 0

    while BFS(graph, source_idx, destination_idx, parent):
        current_capacity = float("Inf")
        curr_node_index = destination_idx

        while curr_node_index != source_idx:
            parent_node_index, edge_id = parent[curr_node_index]
            current_capacity = min(current_capacity, graph[parent_node_index][curr_node_index][edge_id])
            curr_node_index = parent_node_index

        max_capacity += current_capacity
        curr_node_index = destination_idx

        print(source_city, end=' -> ')

        while curr_node_index != source_idx:
            parent_node_index, edge_id = parent[curr_node_index]
            graph[parent_node_index][curr_node_index][edge_id] -= current_capacity

            graph[curr_node_index][parent_node_index].append(current_capacity)
            curr_node_index = parent_node_index

            if adj_matrix.vertex_city[parent_node_index] != source_city:
                print(adj_matrix.vertex_city[parent_node_index], end=' -> ')

        print(f'{destination_city}\nMaximum capacity: {current_capacity}, Total capacity: {max_capacity}\n')

    return max_capacity


source = "New York"
destination = 'San Francisco'

result = EdmondKarp(adj_matrix, source, destination)

print(result)



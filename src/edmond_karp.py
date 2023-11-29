from breadth_first_search import BFS


def EdmondKarp(adj_matrix, source_city, destination_city):
    graph = adj_matrix.graph
    source_idx = adj_matrix.vertex_index[source_city]
    destination_idx = adj_matrix.vertex_index[destination_city]

    n = len(graph)
    parent = [[-1, -1] for _ in range(n)]

    max_capacity = 0

    while BFS(graph, source_idx, destination_idx, parent):
        current_capacity = float("Inf")
        curr_node_index = destination_idx

        print(source_city, end=' -> ')
        layover = None
        while curr_node_index != source_idx:
            parent_node_index, edge_id = parent[curr_node_index]
            current_capacity = min(current_capacity, graph[parent_node_index][curr_node_index][edge_id]['capacity'])

            capacity = graph[parent_node_index][curr_node_index][edge_id]['capacity']
            airline_name = graph[parent_node_index][curr_node_index][edge_id]['airline name']
            plane_model = graph[parent_node_index][curr_node_index][edge_id]['plane model']

            if adj_matrix.vertex_city[parent_node_index] != source_city:
                layover = adj_matrix.vertex_city[parent_node_index]
                print(f"{layover} (operated by {airline_name}: {plane_model}, capacity: {capacity})")

            curr_node_index = parent_node_index

        if layover:
            print(f'{layover} -> {destination_city} (operated by {airline_name}: {plane_model}, capacity: {capacity})\nFlight capacity: {current_capacity}\n')
        else:
            print(f'{destination_city} (operated by {airline_name}: {plane_model})\nFlight capacity: {current_capacity}\n')

        max_capacity += current_capacity
        curr_node_index = destination_idx

        # print(source_city, end=' -> ')

        while curr_node_index != source_idx:
            parent_node_index, edge_id = parent[curr_node_index]
            graph[parent_node_index][curr_node_index][edge_id]['capacity'] -= current_capacity

            reverse_edge = {'capacity': current_capacity}
            graph[curr_node_index][parent_node_index].append(reverse_edge)
            curr_node_index = parent_node_index

        #     if adj_matrix.vertex_city[parent_node_index] != source_city:
        #         print(adj_matrix.vertex_city[parent_node_index], end=' -> ')
        #
        # print(f'{destination_city}\nFlight capacity: {current_capacity}\n')

    return f'Total capacity: {max_capacity}'

def BFS(graph, source, destination, parent):
    """
    Performs a Breadth-First Search on a graph from a source to a destination node.

    Parameters:
    adj_matrix (Graph): The adjacency matrix representing the flight network.
    source (int): The index of the source node in the graph.
    destination (int): The index of the destination node in the graph.
    parent (list): The parent list to store the path from the source to the destination.

    Returns:
    bool: True if a path from source to destination is found, False otherwise.
    """

    n = len(graph)
    visited = [False] * n
    queue = [source]

    visited[source] = True

    while queue:
        vis = queue.pop(0)

        for i in range(n):
            if not visited[i] and len(graph[vis][i]) and sum(plane['capacity'] for plane in graph[vis][i]):
                queue.append(i)
                visited[i] = True

                parent[i] = [vis, graph[vis][i].index(max(graph[vis][i], key=lambda x: x['capacity']))]

    return visited[destination]


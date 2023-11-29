def BFS(graph, source, destination, parent):
    n = len(graph)
    visited = [False] * n
    queue = [source]

    # Set source as visited
    visited[source] = True

    while queue:
        vis = queue.pop(0)

        for i in range(n):
            if not visited[i] and len(graph[vis][i]) and sum(plane['capacity'] for plane in graph[vis][i]):
                # Push the adjacent node in the queue
                queue.append(i)
                visited[i] = True
                parent[i] = [vis, graph[vis][i].index(max(graph[vis][i], key=lambda x: x['capacity']))]

    if visited[destination]:
        return True
    else:
        return False

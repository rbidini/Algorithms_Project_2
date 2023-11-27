from adjacency_matrix import adj_matrix


def BFS(graph, source):
    n = len(graph)
    visited = [False] * n
    queue = [source]

    # Set source as visited
    visited[source] = True

    while queue:
        vis = queue[0]

        # Print current node
        print(vis, end=' ')
        queue.pop(0)

        # For every adjacent vertex to the current vertex
        for i in range(n):
            if graph[vis][i] and not visited[i]:
                # Push the adjacent node in the queue
                queue.append(i)

                visited[i] = True


print(BFS(adj_matrix.graph, 0))

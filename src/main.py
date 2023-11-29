from src.edmond_karp import EdmondKarp
from src.load_adjacency_matrix import load_matrix

# source = input("Source city:")
# destination = input("Destination city:")

source = "New York"
destination = "San Francisco"

adj_matrix = load_matrix(source, destination)

result = EdmondKarp(adj_matrix, source, destination)

print(result)

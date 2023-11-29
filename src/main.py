from src.algorithm.edmond_karp import EdmondKarp
from src.algorithm.load_adjacency_matrix import load_matrix


def run_algorithm(source, destination):
    adj_matrix = load_matrix(source, destination)

    return EdmondKarp(adj_matrix, source, destination)


# source = input("Source city: ").lower()
# destination = input("Destination city: ").lower()

source = "New York".lower()
destination = "San Francisco".lower()

run_algorithm(source, destination)

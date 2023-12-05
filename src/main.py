from algorithm.edmond_karp import MaxCapacity
from algorithm.load_adjacency_matrix import LoadMatrix


def run_algorithm(source, destination):
    """
    Runs the algorithm to calculate the maximum capacity between two cities.

    Parameters:
    source (str): The name of the source city.
    destination (str): The name of the destination city.
    """

    # Load the adjacency matrix.
    load_matrix = LoadMatrix()
    # Returns a tuple where the first element is a boolean indicating the success of the operation,
    # and the second element is either the adjacency matrix or string with error information.
    indicator, result = load_matrix.load(source, destination)

    # Check if the loading of the adjacency matrix was successful
    if not indicator:
        return indicator, result

    main_alg = MaxCapacity()

    # Apply the Edmond-Karp algorithm to find the maximum capacity path within the network.
    return main_alg.edmond_karp(result, source, destination)

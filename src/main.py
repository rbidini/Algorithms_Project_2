from src.algorithm.edmond_karp import EdmondKarp
from src.algorithm.load_adjacency_matrix import load_matrix


def run_algorithm(source, destination):
    adj_matrix = load_matrix(source, destination)

    return EdmondKarp(adj_matrix, source, destination)


# source = input("Source city: ").lower()
# destination = input("Destination city: ").lower()

source = "New York".lower()
destination = "San Francisco".lower()

# result, max_capacity = run_algorithm(source, destination)
# result = sorted(result, key=lambda x: x["maximum capacity"], reverse=True)
#
# for report in result:
#     if report.get('layover'):
#         print(f'{report["source city"]} -> {report["layover"]} (operated by {report["layover airline"]}: {report["layover model"]}) Flight capacity: {report["layover capacity"]}\n'
#               f'{report["layover"]} -> {report["destination city"]} (operated by {report["destination airline"]}: {report["destination model"]}) Flight capacity: {report["destination capacity"]}\n'
#               f'Maximum capacity: {report["maximum capacity"]}\n')
#     else:
#         print(f'{report["source city"]} -> {report["destination city"]} (operated by {report["destination airline"]}: {report["destination model"]}) Flight capacity: {report["maximum capacity"]}\n')
#
# print(f'Total capacity: {max_capacity}')

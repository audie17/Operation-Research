from balas_hammer import find_cost_matrix

def calculate_total_cost(allocation,matrix):
    cost_matrix = find_cost_matrix(matrix)
    total_cost = 0
    for i in range(len(allocation)):
        for j in range(len(allocation[0])):
            total_cost += allocation[i][j] * cost_matrix[i][j]
    return total_cost

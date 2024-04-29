
def find_cost_matrix(data): 
    """
    This function finds the cost matrix from the data
    """
    num_provisions = len(data["Provisions"])
    num_orders = len(data["Orders"])
    cost_matrix = []
    for i in range(num_provisions):
        provision_costs = data["Provisions"]["P"+str(i+1)]
        row = []
        for j in range(num_orders):
            row.append(provision_costs[j])
        cost_matrix.append(row)
    return cost_matrix

def compute_penalties(cost_matrix):
    """
    This function computes the penalties of a given cost matrix
    """
    penalties = []
    for i in range(len(cost_matrix)):
        row = cost_matrix[i]
        sorted_row = sorted(row)
        penalty = sorted_row[1] - sorted_row[0]
        penalties.append(penalty)
    return penalties

def allocate_quantity(cost_matrix):
    """
    This function allocates the maximum possible quantity to the cell with minimum transportation cost
    in the row or column with the largest penalty
    """
    penalties = compute_penalties(cost_matrix)
    max_penalty_index = penalties.index(max(penalties))
    max_penalty_row = cost_matrix[max_penalty_index]
    max_penalty_column = [row[max_penalty_index] for row in cost_matrix]
    min_cost_row_index = max_penalty_row.index(min(max_penalty_row))
    min_cost_column_index = max_penalty_column.index(min(max_penalty_column))
    return min_cost_row_index, min_cost_column_index


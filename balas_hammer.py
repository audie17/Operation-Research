
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
    penalties_row = []
    penalties_column = []
    for i in range(len(cost_matrix)):
        row = cost_matrix[i]
        sorted_row = sorted(row)
        penalty = sorted_row[1] - sorted_row[0]
        penalties_row.append(penalty)
    for j in range(len(cost_matrix[0])):
        column = [row[j] for row in cost_matrix]
        sorted_column = sorted(column)
        penalty = sorted_column[1] - sorted_column[0]
        penalties_column.append(penalty)

    return [penalties_row, penalties_column]

'''
def allocate_quantity(data, cost_matrix):
    """
    This function allocates the maximum possible quantity to the cell with minimum transportation cost
    in the row or column with the largest penalty.
    """
    num_provisions = len(data["Provisions"])
    num_orders = len(data["Orders"])
    total_provisions = data["TotalProvisions"]
    total_orders = data["TotalOrders"]
    result = [[0] * num_orders for _ in range(num_provisions)]

    penalties = compute_penalties(cost_matrix)
    penalties_provisions = penalties[0]
    penalties_orders = penalties[1] 
    max_penalty_row = max(penalties_provisions)
    max_penalty_column = max(penalties_orders)
    
    print(penalties_provisions)
    print(penalties_orders)
    print(max_penalty_row)
    print(max_penalty_column)
    # Find the row or column with the largest penalty
    while penalties_provisions != [] and penalties_orders != []: 

        if max_penalty_row > max_penalty_column:

            for j in range(num_orders):  # Changed from num_provisions to num_orders
                max_penalty_index = penalties_provisions.index(max_penalty_row)
                min_cost = min([cost_matrix[row][max_penalty_index] for row in range(num_provisions)])  # Calculate the minimum cost correctly
                if cost_matrix[max_penalty_index][j] == min_cost:
                    result[max_penalty_index][j] = min(total_provisions[max_penalty_index], total_orders[j])
                    total_provisions[max_penalty_index] -= result[max_penalty_index][j]
                    total_orders[j] -= result[max_penalty_index][j]
                    min_cost = float('inf')  # Reset the minimum cost
            penalties_provisions.pop(max_penalty_index)
            print(penalties_provisions)
            if penalties_provisions != []:
                max_penalty_row = max(penalties_provisions)  # Recalculate max_penalty_row
                print(max_penalty_row)

        else:
            for i in range(num_provisions):  # Changed from num_orders to num_provisions
                max_penalty_index = penalties_orders.index(max_penalty_column)
                min_cost = min([cost_matrix[row][max_penalty_index] for row in range(num_provisions)])  # Calculate the minimum cost correctly
                print(min_cost)
                if cost_matrix[i][max_penalty_index] == min_cost:
                    result[i][max_penalty_index] = min(total_provisions[i], total_orders[max_penalty_index])
                    total_provisions[i] -= result[i][max_penalty_index]
                    total_orders[max_penalty_index] -= result[i][max_penalty_index]
                    min_cost = float('inf')  # Reset the minimum cost
            penalties_orders.pop(max_penalty_index)
            print(penalties_orders)
            if penalties_orders != []:
                max_penalty_column = max(penalties_orders)  # Recalculate max_penalty_column
                print(max_penalty_column)

    return result'''

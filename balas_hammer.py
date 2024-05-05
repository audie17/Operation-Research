
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

def select_max_penalty(cost_matrix):
    """
    This function selects the row or column with the maximum penalty
    """
    penalties = compute_penalties(cost_matrix)
    max_penalty_row = max(penalties[0])
    max_penalty_column = max(penalties[1])

    if max_penalty_row == 0 and max_penalty_column == 0:
        return None

    if max_penalty_row >= max_penalty_column:
        selected_index = ('row', penalties[0].index(max_penalty_row))
    else:
        selected_index = ('column', penalties[1].index(max_penalty_column))

    return selected_index

def ballas_hammer(data):
    orders = data['Orders']
    provisions = data['Provisions']
    provisions_list = list(provisions.values())
    orders_list = list(orders.values())
    costs = find_cost_matrix(data)
    
    # Initialize allocated_costs as a list of lists
    allocated_costs = [[0] * len(orders_list) for _ in range(len(provisions_list))]

    while not all(all(cell == float('inf') for cell in row) for row in costs):
        try:
            selected_index = select_max_penalty(costs)
        except:
            break
        if selected_index is None:
            # break
            debug = 0
        
        if selected_index[0] == 'row':
            selected_row = selected_index[1]
            min_cost = min(costs[selected_row])
            min_cost_index = costs[selected_row].index(min_cost)
            max_supply = min(provisions_list[selected_row], orders_list[min_cost_index])
            allocated_costs[selected_row][min_cost_index] += max_supply  
            provisions_list[selected_row] -= max_supply
            orders_list[min_cost_index] -= max_supply
            costs[selected_row][min_cost_index] = float('inf')  
        else:
            selected_col = selected_index[1]
            col_values = [row[selected_col] for row in costs]
            min_cost = min(col_values)
            min_cost_index = col_values.index(min_cost)
            max_demand = min(provisions_list[min_cost_index], orders_list[selected_col])
            allocated_costs[min_cost_index][selected_col] += max_demand  
            provisions_list[min_cost_index] -= max_demand
            orders_list[selected_col] -= max_demand
            costs[min_cost_index][selected_col] = float('inf')

    # Place remaining costs in the last available cells
    for i in range(len(costs)):
        for j in range(len(costs[0])):
            if costs[i][j] != float('inf'):
                remaining_cost = min(provisions_list[i], orders_list[j])
                allocated_costs[i][j] += remaining_cost
                provisions_list[i] -= remaining_cost
                orders_list[j] -= remaining_cost
                costs[i][j] = float('inf')

    return allocated_costs

def calculate_marginal_costs(cost_matrix):
    if not cost_matrix:
        raise ValueError("Cost matrix is empty")
    
    num_provisions = len(cost_matrix)
    num_orders = len(cost_matrix[0]) if cost_matrix else 0
    
    if num_orders == 0:
        raise ValueError("Cost matrix has no orders")
    
    marginal_costs_provisions = []
    marginal_costs_orders = []
    
    # Calculate marginal costs for provisions
    for row in cost_matrix:
        sorted_row = sorted(row)
        marginal_cost = sorted_row[1] - sorted_row[0]
        marginal_costs_provisions.append(marginal_cost)
    
    # Calculate marginal costs for orders
    for j in range(num_orders):
        column = [row[j] for row in cost_matrix]
        sorted_column = sorted(column)
        marginal_cost = sorted_column[1] - sorted_column[0]
        marginal_costs_orders.append(marginal_cost)
    
    return marginal_costs_provisions, marginal_costs_orders


    


import unittest

class TestCalculateMarginalCosts(unittest.TestCase):
        cost_matrix = [
            [10, 20, 30],
            [15, 25, 35]
        ]
        marginal_costs_provisions, marginal_costs_orders = calculate_marginal_costs(cost_matrix)
        print(marginal_costs_orders)
        print(marginal_costs_provisions)

        # Add more test cases here as needed

if __name__ == '__main__':
    unittest.main()

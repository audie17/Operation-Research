from read_data import read_data_from_file as rd
from display import display_trans_proposals as disp

def north_west_algorithm(matrix):
    provisions = matrix['Provisions']
    orders = matrix['Orders']
    total_provisions = matrix['TotalProvisions']
    total_orders = matrix['TotalOrders']
    
    num_provisions = len(provisions)
    num_orders = len(orders)
    
    result = [[0] * num_orders for _ in range(num_provisions)]
    
    i = 0
    j = 0
    
    while i < num_provisions and j < num_orders:
        if total_provisions[i] == 0:
            i += 1
            continue
        
        if total_orders[j] == 0:
            j += 1
            continue
        
        quantity = min(total_provisions[i], total_orders[j])
        result[i][j] = quantity
        
        total_provisions[i] -= quantity
        total_orders[j] -= quantity
        
        if total_provisions[i] == 0:
            i += 1
        
        if total_orders[j] == 0:
            j += 1
    
    return result

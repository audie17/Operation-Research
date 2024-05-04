# display.py
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------


from read_data import read_data_from_file as rd


def display_matrix(nb):
    """
    Displays the cost matrix along with provisions and orders.
    """
    data_matrice = rd(nb + '.txt')
    cost_matrix = rm(nb + '.txt')
    # Retrieve the number of provisions and orders from the data lengths
    num_provisions = len(data_matrice["Provisions"])
    num_orders = len(data_matrice["Orders"])

    # Create header row with customer labels and 'Provisions' column
    header_row = [' '] + ["C" + str(i+1) for i in range(num_orders)] + ["Provisions"]
    print('\t'.join(header_row))
    
    # Print each provision row
    for i in range(num_provisions):
        provision_label = "P" + str(i+1)
        provision_costs = data_matrice["Provisions"][provision_label]
        provision_total = data_matrice["TotalProvisions"][i]
        row = [provision_label] + ['\033[0;34m' + str(cost) + '\033[0m' for cost in provision_costs] + [provision_total]
        print('\t'.join(map(str, row)))

    # Print the orders row
    orders_row = ["Orders"] + data_matrice["TotalOrders"]
    print('\t'.join(map(str, orders_row)) + '\n')


# Calculate the potentiel cost.
def calculate_potential_costs(allocation, cost_matrix):
    num_provisions = len(allocation)
    num_orders = len(allocation[0])
    
    # Initialize potentials for suppliers (u) and customers (v)
    u = [None] * num_provisions
    v = [None] * num_orders
    
    # Set the first potential (usually u[0]) to 0 as a starting reference
    u[0] = 0
    
    # A simple method to calculate potentials could be a checkerboard method
    changes = True
    while changes:
        changes = False
        for i in range(num_provisions):
            for j in range(num_orders):
                if allocation[i][j] > 0:  # There's a flow between supplier i and customer j
                    if u[i] is not None and v[j] is None:
                        v[j] = cost_matrix[i][j] - u[i]
                        changes = True
                    elif u[i] is None and v[j] is not None:
                        u[i] = cost_matrix[i][j] - v[j]
                        changes = True
    return u, v

# display.py
def display_potentials(u, v):
    """
    Displays the calculated potentials for suppliers (u) and customers (v).
    """
    print("Supplier Potentials (u):")
    print('\t'.join(map(str, u)))
    print("Customer Potentials (v):")
    print('\t'.join(map(str, v)))


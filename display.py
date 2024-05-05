# display.py
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------


from read_data import read_data_from_file as rd

def display_matrix(nb):
    """
    Displays the cost matrix along with provisions and orders.
    """
    data_matrice = rd(nb + '.txt')
    
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
  
# Cost Matrix

def display_cost_matrix(file_name):
    """
    Displays the cost matrix from the specified file.
    """
    # Read the data using the function from read_data.py
    data = rd(file_name+".txt")
    cost_matrix = data["Provisions"]  # assuming cost matrix is stored under "Provisions" key

    num_provisions = len(cost_matrix)
    num_orders = len(data["Orders"])
    
    #initialize a 2d list
    matrix = []
    
    # Iterate over each provision and extract its costs
    for i in range(num_provisions):
        row_label = f"P{i+1}"
        row_costs = cost_matrix[row_label]
        matrix.append(row_costs)
        
    # Print the header row with customer labels
    header_row = [' '] + [f"C{j+1}" for j in range(num_orders)]
    print('\t'.join(header_row))

    # Print each row of the cost matrix
    for i in range(num_provisions):
        row_label = f"P{i+1}"
        row_costs = cost_matrix[row_label]
        print(f"{row_label}\t" + '\t'.join(map(str, row_costs)))

    return matrix  # Ensure this line exists and properly returns the matrix


# Display nordWest

def display_transportation_proposal(transportation_proposal):
    
    for row in transportation_proposal:
        print(" | ".join(map(str, row)))
        
        
#Display marginal cost

def display_marginal_costs(marginal_costs_provisions, marginal_costs_orders):
    """
    Display the marginal costs for each provision and order in a readable format.
    
    Args:
    - marginal_costs_provisions: A list of marginal costs for each provision.
    - marginal_costs_orders: A list of marginal costs for each order.
    """
    # Determine the maximum length of provision and order names
    max_provision_length = max(len("Provision"), max(len(f"P{i+1}") for i in range(len(marginal_costs_provisions))))
    max_order_length = max(len("Order"), max(len(f"C{i+1}") for i in range(len(marginal_costs_orders))))
    
    # Print header
    header = " " * (max_provision_length + 2) + "Provision".center(max_order_length + 2) + " | " + "Order".center(max_order_length + 2)
    print(header)
    
    # Print rows
    num_provisions = len(marginal_costs_provisions)
    num_orders = len(marginal_costs_orders)
    max_length = max(num_provisions, num_orders)
    for i in range(max_length):
        provision_str = f"P{i+1}" if i < num_provisions else ""
        order_str = f"C{i+1}" if i < num_orders else ""
        provision_cost = marginal_costs_provisions[i] if i < num_provisions else ""
        order_cost = marginal_costs_orders[i] if i < num_orders else ""
        row_str = provision_str.ljust(max_provision_length + 2) + str(provision_cost).center(max_order_length + 2) + " | " + order_str.center(max_order_length + 2) + str(order_cost).center(max_order_length + 2)
        print(row_str)
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
    
# Display the matrix with given data
def display_matrix_from_data(data_matrice):
    
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

    # Print the header row with customer labels
    header_row = [' '] + [f"C{j+1}" for j in range(num_orders)]
    print('\t'.join(header_row))

    # Print each row of the cost matrix
    for i in range(num_provisions):
        row_label = f"P{i+1}"
        row_costs = cost_matrix[row_label]
        print(f"{row_label}\t" + '\t'.join(map(str, row_costs)))

    return cost_matrix  # Ensure this line exists and properly returns the matrix


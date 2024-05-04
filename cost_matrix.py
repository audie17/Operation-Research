# cost_matrix.py
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Utility module for displaying the cost matrix of a transportation problem
# ---------------------------------------------------------------------------

from read_data import read_data_from_file

def display_cost_matrix(file_name):
    """
    Displays the cost matrix from the specified file.
    
    Parameters:
        file_name (str): The path to the .txt file containing transportation problem data.
    """
    # Read the data using the function from read_data.py
    data = read_data_from_file(file_name)
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


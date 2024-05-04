# read_data.py
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------

def read_data_from_file(file_name):
    """
    read_data function reads the data from a text file and stores it in memory.
    """
    data = {
        "Provisions": {},
        "Orders": {},
        "TotalOrders": [],
        "TotalProvisions": []
    }
    
    with open(file_name, 'r') as file:
        num_provisions, num_orders = map(int, file.readline().split())

        # Read and store provisions data
        for i in range(num_provisions):
            provision_data = list(map(int, file.readline().split()))
            data["Provisions"]["P"+str(i+1)] = provision_data[:-1]  # Exclude the last column
            data["TotalProvisions"].append(provision_data[-1])  # Add the last column to TotalProvisions

        # Transpose the provisions data to get orders data
        orders_data = list(map(list, zip(*data["Provisions"].values())))

        # Read and store total orders data
        total_orders_data = list(map(int, file.readline().split()))
        data["TotalOrders"] = total_orders_data
        # Store orders data
        for i in range(num_orders):
            data["Orders"]["C"+str(i+1)] = orders_data[i] # Exclude the last row

    return data

def read_data_and_matrix(file_name):
    """
    Read data from file and extract the cost matrix.
    """
    data = read_data_from_file(file_name)
    cost_matrix = [data["Provisions"][f"P{i+1}"] for i in range(len(data["Provisions"]))]
    return cost_matrix


# A matrix is given to this fucntion and it does the same as the read_data_from_file.
def process_matrix_data(matrix):
    
    data = {
        "Provisions": {},
        "Orders": {},
        "TotalOrders": [],
        "TotalProvisions": []
    }
    
    num_provisions = len(matrix)
    if num_provisions == 0:
        return data  # Early return for empty matrix
    num_orders = len(matrix[0]) - 1  # Assuming the last entry in each row is a total provision

    # Process each provision row to extract data
    for i in range(num_provisions):
        provision_data = matrix[i]
        data["Provisions"][f"P{i+1}"] = provision_data[:-1]  # Exclude the last element (total provision)
        data["TotalProvisions"].append(provision_data[-1])  # Last element is the total provision

    # Transpose the provision data to extract orders data
    # Initialize empty lists for each order
    for j in range(num_orders):
        data["Orders"][f"C{j+1}"] = []

    # Fill the orders for each customer
    for provision_key, costs in data["Provisions"].items():
        for j in range(num_orders):
            data["Orders"][f"C{j+1}"].append(costs[j])

    # Calculate total orders for each customer
    data["TotalOrders"] = [sum(data["Orders"][f"C{j+1}"]) for j in range(num_orders)]

    return data

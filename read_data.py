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

        # Store orders data
        for i in range(num_orders):
            data["Orders"]["C"+str(i+1)] = orders_data[i] + [total_orders_data[i]]

        data["TotalOrders"] = total_orders_data

    return data

def read_data_and_matrix(file_name):
    """
    Read data from file and extract the cost matrix.
    """
    data = read_data_from_file(file_name)
    cost_matrix = [data["Provisions"][f"P{i+1}"] for i in range(len(data["Provisions"]))]
    return cost_matrix

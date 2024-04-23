# main.py
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Created By  : Audrey DAMIBA, Melissa LACHEB, Timéo GOGOLACHVILI , Thomas MASSELLES, Zoé LE MAIGUET
# Creation Date: 2024-04-22
# ---------------------------------------------------------------------------

""" This program will perform this perform on graphs representing constraint tables
    Operations availables are:

         1. Read data from text file (.txt) and store in memory.
         2. Display of the following tables :
            ⋆ Cost matrix
            ⋆ Transportation proposal
            ⋆ Potential costs table
            ⋆ Marginal costs table

        3. Algorithm for setting the initial proposal : North-West.
        4. Algorithm for setting the initial proposal : Balas-Hammer.
            ⋆ Calculation of penalties.
            ⋆ Display of row(s) (or columns) with the maximum penalty.
            ⋆ Choice of edge to fill.

        5. Total cost calculation for a given transport proposal.
        6. Solving algorithm : the stepping-stone method with potential.

        
    This project is a part of the course SM602I - Operation Research (L3-INT - 2324S6)
        
        """

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


def main():
    """
    Main function
    """
    file_name = "data.txt"
    data = read_data_from_file("1.txt")
    print(data)

if __name__ == "__main__":
    main()
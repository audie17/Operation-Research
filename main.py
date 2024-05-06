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
import display as disp
import nord_west as nw
import read_data as rd
import balas_hammer as bh
import total_cost as tc
import marginal_cost as marg

def main():
    """
    Main function
    """
    test_nb = int(input("\nWelcome ! \nEnter the Transportation problem number (1 to 12):\n "))
    if 1 <= test_nb <= 12:
        file_name = str(test_nb) +".txt"
        
        print("\n Transportation Problem "+str(test_nb)+":\n")
        
        disp.display_matrix(str(test_nb))
        matrix = rd.read_data_from_file(file_name)
        
        print("\nCost matrix: \n")
        cost_matrix = disp.display_cost_matrix(str(test_nb))  # Make sure to have this function correctly implemented in display.py
        

        print("\nTransportation proposal:\n",
              " - North-West Corner :\n")
        
        result_nw = nw.north_west_algorithm(matrix)
        disp.display_transportation_proposal(result_nw)
        
        print("\n - Balas-Hammer ")
        result_balas = bh.balas_hammer(file_name)
    
        print(result_nw)
        print(" - North-West Corner: ", tc.calculate_total_cost(result_nw,matrix))
        
        print("\nPotential costs table :\n")
        
        print("\nMarginal costs table :\n")
        marginal_costs_provisions, marginal_costs_orders = marg.calculate_marginal_costs(cost_matrix)
        disp.display_marginal_costs(marginal_costs_provisions, marginal_costs_orders)
        
    else:
        print("\nWrong value, it needs to be between 1 and 12.")
        
        
if __name__ == "__main__":
    main()
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

def main():
    """
    Main function
    """
    test_nb = int(input("\nWelcome ! \nEnter the Transportation problem number (1 to 12):\n "))
    if 1 <= test_nb <= 12:
        print("\n Transportation Problem "+str(test_nb)+":\n")
        disp.display_matrix(str(test_nb))
    else:
        print("\nWrong value, it needs to be between 1 and 12.")
        
        
if __name__ == "__main__":
    main()
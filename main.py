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
from read_data import read_data_from_file as rd
import display as disp
import nord_west as nw

def main():
    """
    Main function
    """
    print (" Welcome")
    print(rd('2.txt'))
    nw.north_west_algorithm(rd('2.txt'))
    disp.display_matrix('2')

if __name__ == "__main__":
    main()
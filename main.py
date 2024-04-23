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
            ⋆ Cost matrix V
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

def main():
    """
    Main function
    """
    print (" \nWelcome !\n\nChoose the graph you want to display (Between 1 and 12) : \n")
    
    disp.display_matrix('1')
    
    print("\nTransformation proposal :  \n")
    
    
if __name__ == "__main__":
    main()
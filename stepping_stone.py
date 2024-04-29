from read_data import read_data_from_file as rd
from display import display_matrix as disp

def find_loop(matrix, loop, i, j, loop_cost):
    '''this function will find a loop in a matrix and return True if a loop is found and False otherwise'''
    provisions = matrix['Provisions']
    orders = matrix['Orders']

    for k in range(len(provisions)):
        if k != i and matrix['Costs'][k][j] != 0:
            if (k, j) in loop:
                loop.append((k, j))
                return True
            elif (k, j) not in loop:
                loop.append((k, j))
                loop_cost += matrix['Costs'][k][j]
                return find_loop(matrix, loop, k, j, loop_cost)
    
    for k in range(len(orders)):
        if k != j and matrix['Costs'][i][k] != 0:
            if (i, k) in loop:
                loop.append((i, k))
                return True
            elif (i, k) not in loop:
                loop.append((i, k))
                loop_cost += matrix['Costs'][i][k]
                return find_loop(matrix, loop, i, k, loop_cost)
    
    return False

def stepping_stone(matrix, initial_solution):
    '''this function will perform the stepping stone method on a matrix and its intial result and will return a graph of the results in the form of a dictionary'''
    provisions = matrix['Provisions']
    orders = matrix['Orders']
    total_provisions = matrix['TotalProvisions']
    total_orders = matrix['TotalOrders']

    IBDS = 0
    nb_allocated_cells = 0

    for i in range(len(initial_solution)):
        for j in range(len(initial_solution[0])):
            if initial_solution[i][j] != 0:
                IBDS += initial_solution[i][j] * matrix['Costs'][i][j]
                nb_allocated_cells += 1

    print("Initial Basic Feasible Solution (IBFS) ={} , using {} cells".format(IBDS, nb_allocated_cells))

    if nb_allocated_cells < len(provisions) + len(orders) - 1: #this if check if the initial solution is degenerate
        print("Degeneracy condition detected")
        return
    
    #identify the cells that are un-alocated
    unallocated_cells = []
    for i in range(len(provisions)):
        for j in range(len(orders)):
            if initial_solution[i][j] == 0:
                unallocated_cells.append((i, j))
    nb_unallocated_cells = len(unallocated_cells)

    #calculate potential idenx for each unallocated cell
    potential_indexes = []
    for i, j in unallocated_cells:
        potential_indexes.append((i, j, matrix['Costs'][i][j] - matrix['Potentials'][i] - matrix['Potentials'][j]))
    
    #sort the potential indexes
    potential_indexes.sort(key=lambda x: x[2], reverse=True)
    print("Potential indexes: ", potential_indexes)

    #initialize the graph
    graph = {}
    for i in range(len(provisions)):
        graph[i] = {}
        for j in range(len(orders)):
            graph[i][j] = 0

    #initialize the loop
    loop = []
    loop_found = False
    loop_cost = 0
    while not loop_found:
        #initialize the loop
        loop = []
        loop_cost = 0

        #start the loop
        for i, j, _ in potential_indexes:
            loop = [(i, j)]
            loop_cost = matrix['Costs'][i][j]
            if find_loop(matrix, loop, i, j, loop_cost):
                loop_found = True
                break

    print("Loop found: ", loop)
    print("Loop cost: ", loop_cost)

    #calculate the minimum quantity in the loop
    min_quantity = float('inf')
    for i in range(0, len(loop), 2):
        min_quantity = min(min_quantity, initial_solution[loop[i][0]][loop[i][1]])

    print("Minimum quantity in the loop: ", min_quantity)

    #update the graph
    for i in range(0, len(loop), 2):
        graph[loop[i][0]][loop[i][1]] = initial_solution[loop[i][0]][loop[i][1]] + min_quantity
        graph[loop[i+1][0]][loop[i+1][1]] = initial_solution[loop[i+1][0]][loop[i+1][1]] - min_quantity

    print("Graph: ", graph)

    #update the potentials
    for i in range(len(provisions)):
        for j in range(len(orders)):
            if (i, j) in loop:
                matrix['Potentials'][i] += min_quantity
                matrix['Potentials'][j] -= min_quantity

    print("Potentials: ", matrix['Potentials'])

    return graph

if __name__ == "__main__":
    test_nb = int(input("\nWelcome ! \nEnter the Transportation problem number (1 to 12):\n "))
    if 1 <= test_nb <= 12:
        print("\n Transportation Problem "+str(test_nb)+":\n")
        data_matrice = rd(str(test_nb)+'.txt')
        cost_matrix = disp(str(test_nb))
        initial_solution = [[0] * len(data_matrice['Orders']) for _ in range(len(data_matrice['Provisions']))]
        result = stepping_stone(data_matrice, initial_solution)
        print("Result: ", result)
    else:
        print("\nWrong value, it needs to be between 1 and 12.")
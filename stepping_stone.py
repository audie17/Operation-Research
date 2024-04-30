from read_data import read_data_from_file as rd
from display import display_matrix as disp
from read_data import read_data_and_matrix as rm
from nord_west import north_west_algorithm as nwa

def find_cycle(basic_variables, deltas):
    '''this function is used to find the cycle in the graph'''
    #initialize the cycle
    cycle = []
    
    #initialize the visited nodes
    visited = dict()
    
    #initialize the first node
    for (i, j) in basic_variables:
        visited[(i, j)] = False
    for (i, j) in deltas:
        visited[(i, j)] = False
    
    #find the first node
    for (i, j) in basic_variables:
        if basic_variables[(i, j)] != 0:
            cycle.append((i, j))
            visited[(i, j)] = True
            break
    
    #find the cycle
    while True:
        (x, y) = cycle[-1]
        for (i, j) in basic_variables:
            if (i, j) != (x, y) and basic_variables[(i, j)] != 0 and not visited[(i, j)]:
                cycle.append((i, j))
                visited[(i, j)] = True
                break
        else:
            for (i, j) in deltas:
                if (i, j) != (x, y) and deltas[(i, j)] != 0 and not visited[(i, j)]:
                    cycle.append((i, j))
                    visited[(i, j)] = True
                    break
            else:
                break
    
    return cycle

def stepping_stone(matrix, initial_solution, cost_matrix):
    '''this function is used to find the optimal solution of the transportation problem using the stepping stone method'''
    provisions = matrix['Provisions']
    orders = matrix['Orders']

    #initialize the first graph
    basic_variables = dict()
    for i in range(len(provisions)):
        for j in range(len(orders)):
            if initial_solution[i][j] != 0:
                basic_variables[(i, j)] = initial_solution[i][j]
    
    #check if the solution is degenerate
    if len(basic_variables) != len(provisions) + len(orders) - 1:
        print("The solution is degenerate.")
        #make the solution non-degenerate
        for i in range(len(provisions)):
            for j in range(len(orders)):
                if (i, j) not in basic_variables:
                    basic_variables[(i, j)] = 0
                    break

    #initialize the potentials
    potentials = dict()
    potentials[0] = 0
    
    #initialize the loop variables
    loop = True
    iteration = 0
    while loop and iteration>100:
        iteration += 1
        print("\nIteration ", iteration)
        
        #initialize the deltas
        deltas = dict()
        
        #calculate the deltas
        for i in range(len(provisions)):
            for j in range(len(orders)):
                if (i, j) not in basic_variables:
                    deltas[(i, j)] = cost_matrix[i][j] - (potentials[i] + potentials[len(provisions) + j])
        
        #display the deltas
        print("Deltas: ", deltas)
        
        #find the cycle
        cycle = find_cycle(basic_variables, deltas)
        
        #display the cycle
        print("Cycle: ", cycle)
        
        #find the minimum quantity in the cycle
        min_quantity = None
        for i in range(len(cycle)):
            (x, y) = cycle[i]
            if min_quantity == None or basic_variables[(x, y)] < min_quantity:
                min_quantity = basic_variables[(x, y)]
        
        #display the minimum quantity
        print("Minimum Quantity: ", min_quantity)
        
        #update the basic variables
        for i in range(len(cycle)):
            (x, y) = cycle[i]
            if i % 2 == 0:
                basic_variables[(x, y)] += min_quantity
            else:
                basic_variables[(x, y)] -= min_quantity
        
        #display the basic variables
        print("Basic Variables: ", basic_variables)
        
        #check if the loop should continue
        loop = False
        for i in range(len(provisions)):
            for j in range(len(orders)):
                if (i, j) in basic_variables and basic_variables[(i, j)] != 0:
                    loop = True
                    break

    #calculate the total cost
    total_cost = 0
    for (i, j) in basic_variables:
        total_cost += basic_variables[(i, j)] * cost_matrix[i][j]
    
    #display the total cost
    print("Total Cost: ", total_cost)

    return basic_variables

def disp_graph(dic):
    '''this function is used to display the graph'''
    for i in dic:
        print(i, dic[i])


if __name__ == "__main__":
    for i in range(1, 13):
        print("\n Transportation Problem "+str(i)+":\n")
        data_matrice = rd(str(i)+'.txt')
        cost_matrix = rm(str(i)+'.txt')
        disp(str(i))
        initial_solution = nwa(data_matrice)
        result = stepping_stone(data_matrice, initial_solution, cost_matrix)
        if result!= None:
            disp_graph(result)
    else:
        print("\nWrong value, it needs to be between 1 and 12.")
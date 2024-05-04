from read_data import read_data_from_file as rd
from display import display_matrix as disp
from read_data import read_data_and_matrix as rm
from nord_west import north_west_algorithm as nwa
from math import inf

def into_the_graph(matrix, initial_solution):
    '''this function transforms the initial solution into a graph'''
    provisions = matrix['Provisions']
    orders = matrix['Orders']
    n = len(provisions)
    m = len(orders)
    
    #transform the initial solution into a non-orietended graph
    graph_solution = {}
    for i in range(n):
        graph_solution[i] = []
        for j in range(m):
            if initial_solution[i][j] != 0:
                graph_solution[j] = []
                graph_solution[i].append(j)
                graph_solution[j].append(i)
    #print the graph
    for i in range(n):
        print(i, graph_solution[i])
    return graph_solution
    
def find_E_values(cost_matrix, new_solution):
    '''this functions finds the potential values for the sources and destinations in the graph'''
    #initialize the variables
    num_sources = len(cost_matrix)
    num_destinations = len(cost_matrix[0])

    #initialize the source and destination potentials
    source_E = [-inf]*num_sources
    destination_E = [-inf]*num_destinations
    source_E[0] = 0

    #find the potentials
    for i in range(num_sources):
        for j in range(num_destinations):
            if new_solution[i][j] != 0:
                if source_E[i]==-inf and destination_E[j]!=None:
                    source_E[i] = cost_matrix[i][j] - destination_E[j]
                if destination_E[j]==-inf and source_E[i]!=None:
                    destination_E[j] = cost_matrix[i][j] + source_E[i]
    
    return source_E, destination_E

def find_marginal_costs(cost_matrix, source_E, destination_E):
    '''this function finds the marginal costs for each cell in the solution'''
    #initialize the variables
    num_sources = len(cost_matrix)
    num_destinations = len(cost_matrix[0])
    marginal_costs = [[0]*num_destinations for _ in range(num_sources)]

    #find the marginal costs
    for i in range(num_sources):
        for j in range(num_destinations):
            if source_E[i]!=None and destination_E[j]!=None:
                marginal_costs[i][j] = cost_matrix[i][j] - source_E[i] - destination_E[j]
    
    return marginal_costs

def degenerate_solution(matrix, initial_solution, graph_solution):
    '''this function adds a cell with the smallest cost to the solution if it is degenerate'''
    # Initialize the variables
    provisions = matrix['Provisions']
    orders = matrix['Orders']
    n = len(provisions)
    m = len(orders)
    min_cost = float('inf')
    min_cost_cell = None

    # Go through all the non-allocated cells
    for i in range(n):
        for j in range(m):
            if initial_solution[i][j] == 0:
                # Calculate the cost of adding this cell to the solution
                cost = cost_matrix[i][j] - max_cost_in_loop(graph_solution, i, j)
                # If this cell has the smallest cost, update min_cost and min_cost_cell
                if cost < min_cost:
                    min_cost = cost
                    min_cost_cell = (i, j)

    # Add the cell with the smallest cost to the solution
    if min_cost_cell is not None:
        i, j = min_cost_cell
        initial_solution[i][j] = 0  # Allocate a fictive quantity of zero
        graph_solution[i].append(j)
        graph_solution[j].append(i)

    # Update the number of vertices and edges
    nb_vertices = len(graph_solution)
    nb_edges = sum(len(graph_solution[i]) for i in range(nb_vertices))

    return nb_edges, nb_vertices, initial_solution

def max_cost_in_loop(graph_solution, i, j):
    '''this function finds the maximum cost in the loop containing the cell (i, j)'''
    # Initialize the variables
    max_cost = 0
    current_vertex = i
    current_edge = j

    # Find the loop
    while True:
        next_vertex = None
        for vertex in graph_solution[current_edge]:
            if vertex != current_vertex:
                next_vertex = vertex
                break
        if next_vertex == i or next_vertex is None:
            break
        cost = cost_matrix[current_edge][next_vertex]
        if cost > max_cost:
            max_cost = cost
        current_vertex = current_edge
        current_edge = next_vertex

    return max_cost

def find_loop(graph_solution, i, j):
    '''this function finds the loop containing the cell (i, j)'''
    # Initialize the variables
    loop = [(i, j)]
    current_vertex = i
    current_edge = j

    # Find the loop
    while True:
        next_vertex = None
        for vertex in graph_solution[current_edge]:
            if vertex != current_vertex:
                next_vertex = vertex
                break
        if next_vertex == i:
            break
        loop.append((current_edge, next_vertex))
        current_vertex = current_edge
        current_edge = next_vertex

    return loop

def update_solution(new_solution, marginal_costs, graph_solution):
    '''this function updates the solution by finding the loop with the smallest cost'''
    # Initialize the variables
    n = len(new_solution)
    m = len(new_solution[0])
    min_cost = float('inf')
    min_cost_loop = None

    # Go through all the cells
    for i in range(n):
        for j in range(m):
            if new_solution[i][j] == 0:
                # Find the loop containing this cell
                loop = find_loop(graph_solution, i, j)
                # Calculate the cost of this loop
                cost = sum(marginal_costs[u][v] for u, v in loop)
                # If this loop has the smallest cost, update min_cost and min_cost_loop
                if cost < min_cost:
                    min_cost = cost
                    min_cost_loop = loop

    # Update the solution
    for u, v in min_cost_loop:
        new_solution[u][v] = 0 if new_solution[u][v] > 0 else 1

    return new_solution

def stepping_stone(matrix, initial_solution, cost_matrix):
    '''this function implements the stepping stone method to find the optimal solution, returns the optimal solution under the form of a matrix'''
    # Initialize the variables
    provisions = matrix['Provisions']
    orders = matrix['Orders']
    n = len(provisions)
    m = len(orders)
    
    #transform the initial solution into a non-orietended graph
    graph_solution = into_the_graph(matrix, initial_solution)
    
    #check if the solution is degenerate
    nb_vertices = 0
    nb_edges = 0
    for i in range(len(graph_solution)):
        nb_vertices += 1
        nb_edges += len(graph_solution[i])

    # Add a cell with the smallest cost to the solution if it is degenerate
    iteration = 0
    while abs(nb_edges)!=abs(nb_vertices)-1 and iteration < 1000:
        nb_edges, nb_vertices, new_solution = degenerate_solution(matrix, initial_solution, graph_solution)
        iteration += 1
    
    # Initialize the potentials
    source_E, destination_E = find_E_values(cost_matrix, new_solution)
    
    #intialize the marginal costs
    marginal_costs = find_marginal_costs(cost_matrix, source_E, destination_E)

    #check if the solution is optimal
    optimal = True
    for i in range(n):
        for j in range(m):
            if new_solution[i][j] == 0:
                if marginal_costs[i][j] < 0:
                    optimal = False
                    break
    
    #if the solution is not optimal, find the loop with the smallest cost
    if not optimal:
        new_solution = update_solution(new_solution, marginal_costs, graph_solution)

    return new_solution

if __name__ == "__main__":
    ##for i in range(1, 13):
    i = 1
    print("\n Transportation Problem "+str(i)+":\n")
    data_matrice = rd(str(i)+'.txt')
    cost_matrix = rm(str(i)+'.txt')
    disp(str(i))
    initial_solution = nwa(data_matrice)
    result = stepping_stone(data_matrice, initial_solution, cost_matrix)
    print("\nOptimal Solution:")
    for i in range(len(result)):
        print(i, result[i])
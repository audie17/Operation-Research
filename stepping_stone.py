from read_data import read_data_from_file as rd
from display import display_matrix as disp
from read_data import read_data_and_matrix as rm
from nord_west import north_west_algorithm as nwa
from math import inf
from typing import Dict, List, Tuple

def into_the_graph(matrix: Dict[str, List[int]], initial_solution: List[List[int]]) -> Dict[Tuple[int, str], List[int]]:
    '''this function transforms the initial solution into a graph'''
    provisions = matrix['Provisions']
    orders = matrix['Orders']
    n = len(provisions)
    m = len(orders)
    
    #transform the initial solution into a non-oriented graph
    graph_solution = {}
    for i in range(n):
        if graph_solution.get((i,'p')) == None:
            graph_solution[(i,'p')] = []
        for j in range(m):
            if initial_solution[i][j] != 0:
                if graph_solution.get((j,'o')) == None:
                    graph_solution[(j,'o')] = []
                graph_solution[(i,'p')].append((j,'o'))
                graph_solution[(j,'o')].append((i,'p'))

    return graph_solution

def add_edge(matrix, initial_solution, graph_solution):
    '''this function adds and edge with the smallest cost to the graph representation of the solution among the vertices that already exist in the solution,
    returns the number of edges and vertices in the solution after adding the edge'''
    provisions = matrix['Provisions']
    orders = matrix['Orders']
    n = len(provisions)
    m = len(orders)

    # Initialize the variables
    min_cost = float('inf')
    min_cost_cell = None
    nb_vertices = 0
    nb_edges = 0

    # Find the cell with the smallest cost among the already existing vertices
    for i in range(n):
        for j in range(m):
            if initial_solution[i][j] == 0 and (i,'p') in graph_solution.keys() and (j,'o') in graph_solution.keys():
                if min_cost > initial_solution[i][j]:
                    min_cost = initial_solution[i][j]
                    min_cost_cell = (i,j)

    # Add the cell with the smallest cost to the solution
    if min_cost_cell != None:
        graph_solution[(min_cost_cell[0],'p')].append((min_cost_cell[1],'o'))
        graph_solution[(min_cost_cell[1],'o')].append((min_cost_cell[0],'p'))
        visited_vertices = []
        visited_edges = []
        for key,value in graph_solution.items():
            if key not in visited_vertices:
                visited_vertices.append(key)
                nb_vertices += 1
            for v in value:
                if (key,v) not in visited_edges:
                    visited_edges.append((key,v))
                    nb_edges += 1

    return nb_edges/2, nb_vertices, graph_solution

def remove_edge(matrix, initial_solution, graph_solution):
    '''
    Removes an edge with the highest cost from the graph representation of the solution.

    Args:
        matrix (list): The matrix representing the problem.
        initial_solution (dict): The initial solution.
        graph_solution (dict): The graph representation of the solution.

    Returns:
        tuple: A tuple containing the number of edges and vertices in the solution after removing the edge.

    '''
    # Initialize the variables
    max_cost = -float('inf')
    max_cost_cell = None
    nb_vertices = 0
    nb_edges = 0

    # Find the cell with the highest cost among the already existing edges
    for key,value in graph_solution.items():
        for v in value:
            if initial_solution[key[0]][v[0]] != 0 and initial_solution[key[0]][v[0]] > max_cost:
                max_cost = initial_solution[key[0]][v[0]]
                max_cost_cell = (key[0],v[0])

    # Remove the cell with the highest cost from the solution
    if max_cost_cell != None:
        graph_solution[(max_cost_cell[0],'p')].remove((max_cost_cell[1],'o'))
        graph_solution[(max_cost_cell[1],'o')].remove((max_cost_cell[0],'p'))
        visited_vertices = []
        visited_edges = []
        for key,value in graph_solution.items():
            if key not in visited_vertices:
                visited_vertices.append(key)
                nb_vertices += 1
            for v in value:
                if (key,v) not in visited_edges:
                    visited_edges.append((key,v))
                    nb_edges += 1

    return nb_edges/2, nb_vertices, graph_solution

def find_E_values(cost_matrix, graph_solution):
    '''this function finds the potentials for the source and destination nodes using the cost matrix and the graph representation of the solution'''
    # Initialize the variables
    n = len(cost_matrix)
    m = len(cost_matrix[0])
    source_E = [None]*n
    destination_E = [None]*m
    source_E[0] = 0

    # Find the potentials for the source nodes
    for i in range(n):
        for j in range(m):
            if (j,'o') in graph_solution[(i,'p')] and (i,'p') in graph_solution[(j,'o')]:
                if source_E[i] != None and destination_E[j] == None:
                    destination_E[j] = cost_matrix[i][j] - source_E[i]
                elif source_E[i] == -inf and destination_E[j] != -inf:
                    source_E[i] = cost_matrix[i][j] + destination_E[j]
            elif (j,'o') not in graph_solution[(i,'p')] and (i,'p') not in graph_solution[(j,'o')]:
                if source_E[i] != None and destination_E[j] == None:
                    destination_E[j] = 0
                elif source_E[i] == None and destination_E[j] != None:
                    source_E[i] = 0

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

def find_cycle(graph_solution, cost_matrix):
    '''this function finds the cycle with the smallest cost in the graph representation of the solution'''
    #initialize the variables
    visited = []
    cycle = []
    min_cost = float('inf')

    #find the cycle with the smallest cost
    for key,value in graph_solution.items():
        for v in value:
            
            if (key,v) not in visited:
                visited.append((key,v))
                visited.append((v,key))
                
                if cost_matrix[key[0]][v[0]] < min_cost:
                    min_cost = cost_matrix[key[0]][v[0]]
                    cycle = [key,v]
                    current = v
                    
                    if cycle[0][0] == cycle[1][0]:
                        return cycle
                    
                    iteration = 0
                    while current != cycle[0] and iteration < 10000:
                        print("we are in the while loop, iteration: ", iteration)
                        print("current: ", current)
                        print("cycle[0]: ", cycle[0])
                        print("cycle[1]: ", cycle[1])
                        print("cycle: ", cycle)
                        iteration += 1

                        for v in graph_solution[current]:
                            if (current,v) not in visited:
                                visited.append((current,v))
                                visited.append((v,current))
                                cycle.append(v)
                                current = v
                                break

    return cycle

def stepping_stone(matrix, initial_solution, cost_matrix, depth=0):
    '''
    This function implements the stepping stone method to find the optimal solution.
    
    Args:
        matrix (dict): A dictionary containing the provisions and orders.
        initial_solution (list): The initial solution under the form of a matrix.
        cost_matrix (list): The cost matrix.
    
    Returns:
        list: The optimal solution under the form of a matrix.
    '''
    print("welcome to the stepping stone method, we are at the depth {}, the lower the number, the deeper we are in the recursion\n".format(depth))
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
    visited_vertices = []
    visited_edges = []
    for key,value in graph_solution.items():
        if key not in visited_vertices:
            visited_vertices.append(key)
            nb_vertices += 1
        for v in value:
            if (key,v) not in visited_edges:
                visited_edges.append((key,v))
                nb_edges += 1
    nb_edges = nb_edges/2


    # Add a cell with the smallest cost to the solution if it is degenerate
    iteration = 0
    while abs(nb_edges)!=abs(nb_vertices)-1 and iteration < 10000:

        if abs(nb_edges)>abs(nb_vertices)-1:
            print("we have to remove an edge")
            nb_edges, nb_vertices, graph_solution = remove_edge(matrix, initial_solution, graph_solution)
        elif abs(nb_edges)<abs(nb_vertices)-1:
            print("we have to add an edge")
            nb_edges, nb_vertices, graph_solution = add_edge(matrix, initial_solution, graph_solution)
        else:
            print("there is an error in the code since the solution is not degenerate")
            print ("the result of {} - 1 = {}, so is it equal to {}? {}".format(abs(nb_vertices), abs(nb_edges), abs(nb_vertices)-1, abs(nb_edges)==abs(nb_vertices)-1))
            iteration = inf
            break
        iteration += 1
    
    #find the potentials using the new graph solution
    source_E, destination_E = find_E_values(cost_matrix, graph_solution)

    #find the marginal costs using the new potentials
    marginal_costs = find_marginal_costs(cost_matrix, source_E, destination_E)

    #we check if the solution is optimal
    optimal = True
    for i in range(n):
        for j in range(m):
            if initial_solution[i][j] == 0:
                if marginal_costs[i][j] < 0:
                    optimal = False
                    break
    
    #if the solution is not optimal, we find the cycle with the smallest cost
    if not optimal:
        print("The solution is not optimal")
        cycle = find_cycle(graph_solution, cost_matrix)
        print("Cycle: {} and it's length: {}".format(cycle, len(cycle)))
        min_cost = float('inf')
        for i in range(0,len(cycle),2):
            print("i: {} and i+1: {}".format(i,i+1))
            if min_cost > cost_matrix[cycle[i][0]][cycle[i+1][0]]:
                min_cost = cost_matrix[cycle[i][0]][cycle[i+1][0]]
        print("Min cost: ", min_cost)
        for i in range(0,len(cycle),2):
            print("cycle[i][0]: ", cycle[i][0])
            print("cycle[i+1][0]: ", cycle[i+1][0])
            if i%2 != 0:
                initial_solution[cycle[i][0]][cycle[i+1][0]] += min_cost
            else:
                initial_solution[cycle[i][0]][cycle[i+1][0]] -= min_cost
        print("New solution: ", initial_solution)
        print("here we go again, we are going down\n")
        initial_solution = stepping_stone(matrix, initial_solution, cost_matrix, depth - 1)
        print("we are back to the previous depth {}, we are going up".format(depth))

    else:
        print("The solution is optimal, the final depth is: ", depth)

    return initial_solution

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
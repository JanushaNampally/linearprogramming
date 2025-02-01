import numpy as np
from simplex_method import simplex 
from transportation import solve_transportation_problem
from graphical_method import solve_linear_program

def main():
    c = [9, 10, 7]
    A = [[1, 3, 2], [4, 1, 3], [2, 4, 1]]
    b = [12, 16, 14]
    solution, optimal_value = simplex(np.array(c), np.array(A), np.array(b))
    print("\nSimplex Method:")
    print("Optimal solution: ", solution)
    print("Optimal Value:", optimal_value)
    
    
    cost_matrix = [[2, 3, 1], [5, 4, 8], [5, 6, 8]]
    supply = [20, 30, 25]
    demand = [10, 25, 40]
    result = solve_transportation_problem(cost_matrix, supply, demand)
    print("\nTransportation Problem: ")
    print("Solution: \n", result["solution"])
    print("Total Cost:", result["total_cost"])
    print("Status:", result["status"])
    
    c = [5, 4]
    A = [[1, 2], [3, 1], [-1, 0], [0, -1]]
    b = [20, 30 , 0, 0]
    
    print("\nGraphical Method:")
    solve_linear_program(c,A,b)
    
if __name__ == "__main__":
    main()

    
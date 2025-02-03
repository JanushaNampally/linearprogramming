import numpy as np 

def simplex():
    """
    Solves the Linear Programming problem using the Simplex Method with user input.
    """
    opt_type = input("Enter optimization type (max/min): ").strip().lower()
    
    num_variables = int(input("Enter number of variables: "))
    num_constraints = int(input("Enter number of constraints: "))
    
    print("Enter coefficients of the objective function (separated by space):")
    c = np.array(list(map(float, input().split())))
    if opt_type == "min":
        c = -c  # Convert to maximization problem
    
    print("Enter the coefficient matrix (each row separated by newline):")
    A = np.array([list(map(float, input().split())) for _ in range(num_constraints)])
    
    print("Enter the right-hand side values (separated by space):")
    b = np.array(list(map(float, input().split())))
    
    # Add slack variables
    slack_vars = np.eye(num_constraints)
    tableau = np.hstack((A, slack_vars, b.reshape(-1, 1)))
    
    # Add objective function row
    obj_row = np.hstack((-c, np.zeros(num_constraints + 1)))
    tableau = np.vstack((tableau, obj_row))
    
    num_total_vars = num_variables + num_constraints
    
    # Start Simplex iterations
    while True:
        if all(tableau[-1, :-1] >= 0):
            break
        
        pivot_col = np.argmin(tableau[-1, :-1])
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios <= 0] = np.inf
        pivot_row = np.argmin(ratios)
        
        if np.all(ratios == np.inf):
            print("The problem is unbounded.")
            return
        
        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element
        
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]
    
    # Extract solution
    solution = np.zeros(num_total_vars)
    for i in range(num_constraints):
        basic_var_index = np.where(tableau[i, :-1] == 1)[0]
        if len(basic_var_index) == 1 and basic_var_index[0] < num_total_vars:
            solution[basic_var_index[0]] = tableau[i, -1]
    
    optimal_value = tableau[-1, -1]
    
    print("Optimal Solution:", solution[:num_variables])
    print("Optimal Value:", optimal_value if opt_type == "max" else -optimal_value)

if __name__ == "__main__":
    simplex()

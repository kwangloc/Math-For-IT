import numpy as np

def two_phase_simplex(c, A, b):
    m, n = A.shape
    # Add artificial variables to convert to standard form
    c_phase1 = np.concatenate([np.zeros(n), np.ones(m)])
    A_phase1 = np.concatenate([A, np.eye(m)], axis=1)
    c_phase2 = c
    A_phase2 = A

    # Phase 1: Solve the auxiliary linear programming problem
    x_phase1, tableau_phase1 = simplex_method(c_phase1, A_phase1, b)

    # Check if the optimal value in the auxiliary problem is zero
    if tableau_phase1[-1, -1] > 1e-10:
        print("The original problem is infeasible.")
        return None

    # Remove artificial variables from the basis
    non_basic_indices = np.where(x_phase1 == 0)[0]
    A_phase2 = np.delete(A_phase2, non_basic_indices, axis=1)
    c_phase2 = np.delete(c_phase2, non_basic_indices)

    # Phase 2: Solve the original linear programming problem
    x_phase2, tableau_phase2 = simplex_method(c_phase2, A_phase2, b)

    return x_phase2, tableau_phase2

def simplex_method(c, A, b):
    m, n = A.shape
    tableau = np.hstack([A, np.eye(m), b.reshape(-1, 1)])
    c_bar = np.concatenate([c, np.zeros(m)])
    basic_indices = np.arange(n, n + m)

    while np.any(c_bar > 0):
        entering_index = np.argmax(c_bar)
        ratios = tableau[:-1, -1] / tableau[:-1, entering_index]

        if np.all(ratios <= 0):
            print("The problem is unbounded.")
            return None

        leaving_index = np.argmin(ratios)
        pivot = tableau[leaving_index, entering_index]
        tableau[leaving_index, :] /= pivot

        for i in range(m + 1):
            if i != leaving_index:
                tableau[i, :] -= tableau[i, entering_index] * tableau[leaving_index, entering_index]

        basic_indices[leaving_index] = entering_index
        c_bar -= c_bar[entering_index] * tableau[leaving_index, :]

    x = np.zeros(n)
    x[basic_indices < n] = tableau[:-1, -1]
    return x, tableau


# Example usage:
c = np.array([-3, -2])
A = np.array([[1, -1], [3, 1], [4, 3]])
b = np.array([2, 5, 7])

result = two_phase_simplex(c, A, b)
if result:
    x_optimal, tableau_optimal = result
    print("Optimal solution:", x_optimal)
    print("Optimal value:", np.dot(c, x_optimal))

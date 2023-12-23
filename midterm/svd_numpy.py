import numpy as np

def svd_decomposition(matrix):
    # Perform Singular Value Decomposition
    U, S, V = np.linalg.svd(matrix, full_matrices=True)

    # U, S, and V are matrices such that matrix = U @ np.diag(S) @ V
    return U, S, V

def main():
    # Define a sample matrix
    # matrix = np.array([[1, 2, 3],
    #                    [4, 5, 6],
    #                    [7, 8, 9]])
    
    # matrix = np.array([[1, -0.8],
    #                    [0, 1],
    #                    [1, 0]])
    matrix = np.array([[1, 2, 3],
                       [1, 2, 4],
                       [1, 2, 5]])

    # Perform SVD decomposition
    U, S, V = svd_decomposition(matrix)

    # Display the results
    print("Original Matrix:")
    print(matrix)
    print("\nU matrix:")
    print(U)
    print("\nS (Singular Values) matrix:")
    print(np.diag(S))
    print("\nV matrix:")
    print(V)

if __name__ == "__main__":
    main()



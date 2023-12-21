import numpy as np

def svd_decomposition(matrix):
    # Tính chỉ số riêng, vector riêng của ma trận chuyển vị A^T
    eigenvalues, Vt = np.linalg.eig(matrix.T @ matrix)
    
    # Sắp xếp các chỉ số riêng, vector riêng tương ứng theo thứ tự giảm dần
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    Vt = Vt[:, sorted_indices]
    
    # Tính singular_value và sắp xếp
    singular_values = np.sqrt(eigenvalues)
    
    # Tính nghịch đảo singular_value
    singular_values_inv = 1.0 / singular_values
    print("singular_values_inv")
    print(singular_values_inv)

    # Tính ma trận U
    U = matrix @ Vt @ np.diag(singular_values_inv)
    
    return U, singular_values, Vt.T

def main():
    matrix2 = np.array([[1, -0.8],
                       [0, 1],
                       [1, 0]])
    
    matrix = np.array([[2, -1],
                       [2, 2],])
    
    # matrix = np.array([
    #     [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5]
    # ])

    U, S, V = svd_decomposition(matrix)

    print("Original Matrix A:")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # print(round(matrix[j][i], 3), end="  ")
            print(matrix[i][j], end="  ")
        print()

    print("\nU matrix:")
    # print(U)
    for i in range(len(U)):
        for j in range(len(U[0])):
            print(round(U[i][j], 3), end="  ")
        print()

    print("\nD (Singular Values) matrix:")
    # print(np.diag(S))
    D = np.diag(S)
    for i in range(len(D)):
        for j in range(len(D[0])):
            print(round(D[i][j], 3), end="  ")
        print()


    print("\nV^T matrix:")
    # print(V)
    for i in range(len(V)):
        for j in range(len(V[0])):
            print(round(V[i][j], 3), end="\t")
        print()

if __name__ == "__main__":
    main()

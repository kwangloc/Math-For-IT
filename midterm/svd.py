import math

def svd(matrix):
    # Bước 1: Tính A^T * A và A * A^T
    m, n = len(matrix), len(matrix[0])
    print(f"m={m}, n={n}")
    ATA = [[0] * n for _ in range(n)]
    AAT = [[0] * m for _ in range(m)]

    for i in range(n):
        for j in range(n):
            for k in range(m):
                ATA[i][j] += matrix[k][i] * matrix[k][j]

    for i in range(m):
        for j in range(m):
            for k in range(n):
                AAT[i][j] += matrix[i][k] * matrix[j][k]

    # Bước 2: Tính eigenvalues và eigenvectors của A^T * A
    eigenvalues, V = jacobi_eigenvalue(ATA)

    # Bước 3: Tính sigma từ eigenvalues
    sigma = [math.sqrt(eigenvalue) for eigenvalue in eigenvalues]

    # Bước 4: Tính U và VT từ A và V
    U = [[0] * m for _ in range(n)]
    VT = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            VT[i][j] = V[i][j]

    print(f"length check: {len(matrix)}, {len(V)}, {len(sigma)}")
    print("matrix: ") 
    print(matrix)
    print("V: ")
    print(V)
    print("sigma: ")
    print(sigma)
    print("U: ")
    print(U)
    
    # for i in range(n):
    #     for j in range(m):
    #         for k in range(n):
    #             U[j][i] += matrix[j][k] * V[k][i] / sigma[i]

    for i in range(n):
        for j in range(m):
            for k in range(len(V)):
                U[i][j] += matrix[j][k] * V[k][i] / sigma[i]

    return U, sigma, VT

def jacobi_eigenvalue(A, max_iterations=1000, epsilon=1e-6):
    n = len(A)
    V = [[0.0] * n for _ in range(n)]  # Initialize the transformation matrix as an identity matrix
    for i in range(n):
        V[i][i] = 1.0

    for _ in range(max_iterations):
        max_val = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j

        if max_val < epsilon:
            break

        theta = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
        c = math.cos(theta)
        s = math.sin(theta)

        for i in range(n):
            temp = A[p][i]
            A[p][i] = c * temp + s * A[q][i]
            A[q][i] = -s * temp + c * A[q][i]
            temp = A[i][p]
            A[i][p] = c * temp + s * A[i][q]
            A[i][q] = -s * temp + c * A[i][q]
            temp = V[i][p]
            V[i][p] = c * temp + s * V[i][q]
            V[i][q] = -s * temp + c * V[i][q]

    eigenvalues = [A[i][i] for i in range(n)]
    eigenvectors = V
    return eigenvalues, eigenvectors


def main():
    # A = [[2, 1], [1, 3]]
    A = [
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5],
    ]
    B = [
        [1, -0.8],
        [0, 1],
        [1, 0]
    ]
    U, sigma, VT = svd(B)
    print("U matrix:")
    for i in range(len(U)):
        for j in range(len(U)):
            print(U[i][j], end="  ")
        print()
    
    print("Sigma matrix:")
    print(sigma)
    # for i in range(len(sigma)):
    #     for j in range(len(sigma)):
    #         print(sigma[i][j], end="\t")
    #     print()
    
    print("VT matrix:")
    for i in range(len(VT)):
        for j in range(len(VT)):
            print(VT[i][j], end="  ")
        print()

if __name__ == "__main__":
    main()